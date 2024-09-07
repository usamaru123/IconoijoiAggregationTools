from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import MenberModel , VenueModel

import plotly.graph_objects as go
import kaleido
import logging
from . import graph





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



    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution,'interval',seconds=30)
    scheduler.start()