from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging
from . import graph

logfile = "./test.log"
logging.basicConfig(filename=logfile,level=logging.WARNING)


def periodic_execution():

    venues = VenueModel.objects.all()
    
    

    for venue in venues:
        venue_id   = venue.venueid
        block_type = venue.blocktype.id
        row_max    = venue.rowmax
        column_max = venue.columnmax

        item = {}
        histgrams = {}

        floorvalobj = venue.floor.order_by('priority')
        sheetvalobj = venue.sheettype.order_by('priority')

        floorsval = [item.floorname for item in floorvalobj]
        sheetsval = [item.sheet for item in sheetvalobj]

        qsmodel = MenberModel.objects.filter(venueid=venue_id).all()
        qsrow = qsmodel.exclude(row1__exact="")

        if(block_type==1): #座席集計タイプ参照
            for i in range(len(floorsval)):
                qs_f = qsrow.filter(floor1=floorsval[i])
                if len(qs_f) > 0:
                        for j in range(len(sheetsval)):
                            qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                            item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                            histgrams[floorsval[i]] = graph.Floor_Histgram(venue_id,item,floorsval[i])
            #logging.info(str(venue_id)+"_"+datetime.now().strftime('%Y/%m/%d %H:%M:%S')+"_type:"+str(block_type))
        elif(block_type==2):
            block  = [item.block_r1 for item in qsmodel]
            column = [item.block_c1 for item in qsmodel]
            sheet  = [item.sheet1   for item in qsmodel]
            graph.Arena_HeatMap(venue_id,block,column,sheet,row_max,column_max)

            for i in range(1,len(floorsval)):
                qs_f = qsrow.filter(floor1=floorsval[i])
                if len(qs_f) > 0:
                        for j in range(len(sheetsval)):
                            qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                            item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                            histgrams[floorsval[i]] = graph.Floor_Histgram(venue_id,item,floorsval[i])

    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()