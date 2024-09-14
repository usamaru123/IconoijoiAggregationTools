from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging
from . import graph
import datetime

today = datetime.date.today().strftime('%Y%m%d')
logfile = "./logs/scheduler_"+today+".log"
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

        venue_floorobj = venue.floor.order_by('priority')
        venue_sheetobj = venue.sheettype.order_by('priority')

        venue_floors = [item.floorname for item in venue_floorobj]
        venue_sheets = [item.sheet for item in venue_sheetobj]

        results = MenberModel.objects.filter(venueid=venue_id).all()
        results_row = results.exclude(row1__exact="")

        if(block_type==1): #座席集計タイプ参照
            for i in range(len(venue_floors)):
                floor_results = results_row.filter(floor1=venue_floors[i])
                if len(floor_results) > 0:
                        for j in range(len(venue_sheets)):
                            sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                            item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                            histgrams[venue_floors[i]] = graph.Floor_Histgram(venue_id,item,venue_floors[i])
                        
        elif(block_type==2):
            for venue_sheet in venue_sheets:
                results_sheet = results.filter(sheet1=venue_sheet , floor1=venue_floors[1])

                block  = [item.block_r1 for item in results_sheet]
                column = [item.block_c1 for item in results_sheet]

                graph.Arena_HeatMap(venue_id,venue_sheet,row_max,column_max,block,column)

            for i in range(1,len(venue_floors)):
                floor_results = results_row.filter(floor1=venue_floors[i])
                if len(floor_results) > 0:
                        for j in range(len(venue_sheets)):
                            sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                            item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                            histgrams[venue_floors[i]] = graph.Floor_Histgram(venue_id,item,venue_floors[i])

    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()