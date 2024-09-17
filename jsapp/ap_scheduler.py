from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging
from . import graph
import datetime




def periodic_execution():
    today = datetime.date.today().strftime('%Y%m%d')
    time = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')

    venues = VenueModel.objects.all()
    returns_val = 0

    logfile = "./logs/scheduler_"+today+".log"
    logging.basicConfig(filename=logfile,level=logging.INFO)

    colors     = ['tempo','PuRd','Oranges','Blues','BuGn','Purples']
    colorcount = 0
    
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

        if(len(results) == 1):
            logging.warning(time + '_' + str(venue_id) + ':新規公演に回答が追加されました。')
        elif(len(results) == 100):
            logging.warning(time + '_' + str(venue_id) + ':回答が100件を超えました。')
        elif(len(results) == 1000):
            logging.warning(time + '_' + str(venue_id) + ':回答が1000件を超えました。')            


        if(block_type==1): #座席集計タイプ参照
            for i in range(len(venue_floors)):
                floor_results = results_row.filter(floor1=venue_floors[i])
                if len(floor_results) > 0:
                        for j in range(len(venue_sheets)):
                            sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                            item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                            graph.Floor_Histgram(venue_id,item,venue_floors[i])

                        
        elif(block_type==2):
            colorcount = 1
            title = '合計'
            results_arena = results.filter(floor1=venue_floors[0])
            block  = [item.block_r1 for item in results_arena]
            column = [item.block_c1 for item in results_arena]
            graph.Arena_HeatMap(venue_id,title,row_max,column_max,block,column,time,colors[0])


            for venue_sheet in venue_sheets:
                results_sheet = results_arena.filter(sheet1=venue_sheet)

                block  = [item.block_r1 for item in results_sheet]
                column = [item.block_c1 for item in results_sheet]

                graph.Arena_HeatMap(venue_id,venue_sheet,row_max,column_max,block,column,time,colors[colorcount])

                colorcount += 1

            for i in range(1,len(venue_floors)):
                floor_results = results_row.filter(floor1=venue_floors[i])
                if len(floor_results) > 0:
                        for j in range(len(venue_sheets)):
                            sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                            item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                            graph.Floor_Histgram(venue_id,item,venue_floors[i])
    #logging.WARNING(time +'_graphreturn_' + str(returns_val))
    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()