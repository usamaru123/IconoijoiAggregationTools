from datetime import datetime,date
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging

logger = logging.getLogger(__name__)

def periodic_execution():

    venues = VenueModel.objects.all()


    venueids_val = [venue.venueid for venue in venues]
    

    for i in range (len(venueids_val)): 
        item = {}
        histgrams = {}
        venue_id = venueids_val[i]
        qsmodel = MenberModel.objects.filter(venueid=venue_id).all()
        logger.info(venue_id)
        qsrow = qsmodel.exclude(row1__exact="")

        floorsval = ['1LEVEL','3LEVEL','5LEVEL','7LEVEL']
        sheetsval = ['グッズ付きアリーナエリア','一般席','女性エリア席','カメコエリア席','着席指定席']

        for i in range(len(floorsval)):
            qs_f = qsrow.filter(floor1=floorsval[i])
            if len(qs_f) > 0:
                    for j in range(len(sheetsval)):
                        qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                        item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                        histgrams[floorsval[i]] = Floor_Histgram(venue_id,item,floorsval[i])
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
    
    fig.write_image("../temp/"+venueid+"_"+title+".jpg",format='jpeg',scale=2,validate=False,engine='kaleido')
    return 


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',minutes=1)
    scheduler.start()