from datetime import datetime,date
from apscheduler.schedulers.background import BackgroundScheuler

from .models import MenberModel

import plotly.graph_objects as go
import kaleido



def Floor_Histgram():
    qs_f_sheet = {}
    histgrams = {}
    item = {}

    qsmodel = MenberModel.objects.filter(venueid='2024010201').all()
    qsrow = qsmodel.exclude(row1__exact="")

    floorsval = ['1LEVEL','3LEVEL','5LEVEL','7LEVEL']
    sheetsval = ['グッズ付きアリーナエリア','一般席','女性エリア席','カメコエリア席','着席指定席']

    for i in range(len(floorsval)):
        qs_f = qsrow.filter(floor1=floorsval[i])
        if len(qs_f) > 0:
                for j in range(len(sheetsval)):
                    qs_f_sheet = qs_f.filter(sheet1=sheetsval[j])
                    item[sheetsval[j]] = [int(row.row1 or 0) for row in qs_f_sheet]
                    histgrams[floorsval[i]] = Floor_Histgram(item,floorsval[i])



    def Floor_Histgram(item,title):
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
        
        fig.write_image("../"+title+".jpg",format='jpeg',scale=2,validate=False,engine='kaleido')
        return 


def start():
    scheduler = BackgroundScheuler()
    scheduler.add_job(Floor_Histgram,'interval',minutes=1)