from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging

logfile = "./test.log"
logging.basicConfig(filename=logfile,level=logging.DEBUG)


def periodic_execution():

    venues = VenueModel.objects.all()
    
    

    for venue in venues:
        venue_id = venue.venueid
        item = {}
        histgrams = {}

        floorvalobj = venue.floor.order_by('priority')
        sheetvalobj = venue.sheettype.order_by('priority')

        floorsval = [item.floorname for item in floorvalobj]
        sheetsval = [item.sheet for item in sheetvalobj]

        qsmodel = MenberModel.objects.filter(venueid=venue_id).all()
        qsrow = qsmodel.exclude(row1__exact="")


        for i in range(len(floorsval)):
            qs_f = qsrow.filter(floor1=floorsval[i])
            if len(qs_f) > 0:
                    for j in range(len(sheetsval)):
                        qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                        item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                        histgrams[floorsval[i]] = Floor_Histgram(venue_id,item,floorsval[i])
        logging.info(str(venue_id)+"_"+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    return


def Floor_Histgram(venueid,item,title):
    if (item is None):
        return

    itemlist = list(item.keys())

    fig = go.Figure(

    )
    
    for sheet in itemlist:
        fig.add_trace(go.Histogram(y=item[sheet],name=sheet))


    fig.update_traces(xbins=dict(start=1,
                                end=50,
                                size=1),
                    opacity=1
                    )
    
    fig.update_layout(barmode='stack')
    fig.update_layout(legend=dict(yanchor="bottom",
                            y=0.95,
                            xanchor="right",
                            x=0.97))
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0), 
    )
    fig.update_yaxes(autorange='reversed')
    
    fig.write_image("/home/shun/IconoijoiAggregationTools/temp/"+str(venueid)+"_"+title+".jpg",format='jpeg',scale=2,validate=False,engine='kaleido')
    return 


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()