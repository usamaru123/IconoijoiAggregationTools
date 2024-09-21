from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel ,TicketTypeModel

import plotly.graph_objects as go
import kaleido
import logging
from . import graph
import datetime




def periodic_execution():
    today = datetime.date.today().strftime('%Y%m%d')
    time = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')


    logfile = "./logs/scheduler_"+today+".log"
    logging.basicConfig(filename=logfile,level=logging.INFO)



    ticketmodel = TicketTypeModel.objects.order_by('priority').all()
    venuemodel = VenueModel.objects.all()
    returns_val = 0

    venue_tickets = [ticket.dispticketname for ticket in ticketmodel]
    
    for venue in venuemodel:
        venue_id   = venue.venueid
        if(venue.batchflag):



            venue_salesobj  = venue.salestype.order_by('priority')
            venue_floorobj  = venue.floor.order_by('priority')
            venue_sheetobj  = venue.sheettype.order_by('priority')
            perform_timeobj = venue.perform_time.order_by('disp_priority')

            venue_sales  = [item.dispsalesname for item in venue_salesobj]
            venue_floors = [item.floorname for item in venue_floorobj]
            venue_sheets = [item.sheet for item in venue_sheetobj]
            perform_times = [item.perform_time for item in perform_timeobj]

            results = MenberModel.objects.filter(venueid=venue_id).all()
            

            salesval   = [item.sale1   for item in results]
            ticketsval = [item.ticket1 for item in results]
            sheetsval  = [item.sheet1  for item in results]
            floorsval  = [item.floor1  for item in results]

            graph.piecreate(venue_id,salesval,venue_sales,'販売種別割合',time)
            graph.piecreate(venue_id,ticketsval,venue_tickets,'チケット割合',time)
            graph.piecreate(venue_id,sheetsval,venue_sheets,'座席割合',time)
            graph.piecreate(venue_id,floorsval,venue_floors,'階層割合',time)


            if(perform_times.count()==1):
                createHistgrams(venue,venue_floors,venue_sheets,perform_times[i],results ,time)
            else:
                for i in range(2):
                    createHistgrams(venue,venue_floors,venue_sheets,perform_times[i],results,time)
  
            logging.info( '[PROCESS:'+str(venue_id) + '_定期画像出力_' + time + ']' +  ':実行完了しました')
        else: 
            logging.info( '[PROCESS:'+str(venue_id) + '_定期画像出力_' + time + ']' +  ':Batchflag=Falseのため実行しませんでした')
    return


def createHistgrams(venue,venue_floors,venue_sheets,perform_time,results,time):
    colors     = ['tempo','PuRd','Oranges','Blues','BuGn','Purples']
    colorcount = 0

    item = {}
    histgrams = {}
    venue_id    = venue.venueid
    block_type = venue.blocktype.id
    row_max    = venue.rowmax
    column_max = venue.columnmax
    results_row = results.exclude(row1__exact="")

    if(block_type==1): #座席集計タイプ参照
        for i in range(len(venue_floors)):
            floor_results = results_row.filter(floor1=venue_floors[i])
            if len(floor_results) > 0:
                    for j in range(len(venue_sheets)):
                        sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                        item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                        graph.Floor_Histgram(venue_id,perform_time,item,venue_floors[i],time)

                            
            elif(block_type==2):
                colorcount = 1
                title = '合計'
                results_arena = results.filter(floor1=venue_floors[0])
                block  = [item.block_r1 for item in results_arena]
                column = [item.block_c1 for item in results_arena]
                graph.Arena_HeatMap(venue_id,perform_time,title,row_max,column_max,block,column,time,colors[0])


                for venue_sheet in venue_sheets:
                    results_sheet = results_arena.filter(sheet1=venue_sheet)

                    block  = [item.block_r1 for item in results_sheet]
                    column = [item.block_c1 for item in results_sheet]

                    graph.Arena_HeatMap(venue_id,perform_time,venue_sheet,row_max,column_max,block,column,time,colors[colorcount])

                    colorcount += 1

                for i in range(1,len(venue_floors)):
                    floor_results = results_row.filter(floor1=venue_floors[i])
                    if len(floor_results) > 0:
                            for j in range(len(venue_sheets)):
                                sheet_results = floor_results.filter(sheet1=venue_sheets[j])
                                item[venue_sheets[j]] = [int(row.row1 or 0) for row in sheet_results]
                                graph.Floor_Histgram(venue_id,perform_time ,item,venue_floors[i],time)
    

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()