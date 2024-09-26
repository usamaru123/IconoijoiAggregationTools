import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px
from plotly.offline import plot
import pandas as pd
import numpy as np

import logging
import datetime

today = datetime.date.today().strftime('%Y%m%d')

logfile = "./logs/graph_"+today+".log"
logging.basicConfig(filename=logfile,level=logging.INFO)


def Arena_HeatMap(venueid,perform_time ,venue_sheet,rowmax,columnmax,rows,columns,time,color):
    columnlist = []
    rowlist = []

    row = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if (rows is None):
        logging.info('<arenacreate>'+time+'_'+str(venueid) + '_' + venue_sheet+ '_' +  str(int_rows)+":データ数が０です。")
        return
    
    if(len(rows) != len(columns)):
        logging.info('<arenacreate>'+time+'_'+str(venueid) + '_' + venue_sheet+ '_' +  str(int_rows)+":データ数が０です。")
        return 
        
    for i in range(0,columnmax):
        columnlist.append(i+1)

    for i in range(0,rowmax):
        rowlist.append(row[i])

    block = listcreate(rowlist,columnlist)

    int_columns = []
    int_rows = []

    try:
    #列と行をint型に変換
        for i in range(len(rows)):
            if (rows[i] != ''):        
                    int_rows.append(rows[i])

        for i in range(len(columns)):
            if (columns[i] != ''):        
                    int_columns.append(int(columns[i]))
    except:
        logging.error('<arenacreate>'+time+'_'+str(venueid)+ '_' +perform_time + '_' + venue_sheet+ '_' +  str(int_rows[i])+":int型に変換できませんでした。")


    if len(int_columns)==0 or len(int_rows)==0:
        logging.debug('<arenacreate>'+time+'_'+str(venueid)+ '_' +perform_time + '_' + venue_sheet+ '_' +  str(int_rows)+":データ数が０です。")
        return 
    
            

    for i in range(len(int_rows)):
        try:
            block[int_columns[i]][int_rows[i]] +=1
        except:
            logging.warning('<arenacreate>'+time+'_'+str(venueid)+ '_' +perform_time + '_' + venue_sheet+ '_' +  str(int_rows[i])+'_' + str(int_columns[i])+ ":座席がリスト外です。拡張してください。")



    blockdf = pd.DataFrame(block)

    fig = go.Figure(
    )


    fig.add_trace(
            go.Heatmap
        (
            z=blockdf.values.tolist(),
            x=blockdf.columns.tolist(),
            y=blockdf.index.tolist(),        
            texttemplate="%{z}",
            colorscale=color,   
            zmax = 10,
            zmin = 0,
            xgap=2,
            ygap=2
        )
    )

    fig.update_layout(
				font=dict(size=20),
        height=500,
        margin_l=0,
        margin_r=0,
        title=dict(text='<b>ブロックごとの集計結果：'+venue_sheet,
                   font=dict(size=20)
                 ),
    )
    fig.update_layout(
    xaxis_title=dict(
                    text=time+"時点",
                    font=dict(size=15),
                    standoff=50
        )
    )

    fig.update_traces(showscale=False)
    fig.update_yaxes(autorange='reversed',dtick=1)
    fig.update_xaxes(dtick=1)
    
		

    fig.write_image("/home/shun/IconoijoiAggregationTools/media/" + str(venueid) + "_arena_" + perform_time +'_' + venue_sheet+".jpg",format='jpeg',scale=2,validate=False,engine='kaleido')
    logging.debug('<arenacreate>'+time+'_'+str(venueid) + '_' +perform_time + '_'+ venue_sheet+":出力完了")

    return 
 




def Floor_Histgram(venueid,perform_time ,item,title,time):
    if (item is None):
        logging.debug('<floorhistgram>'+time+'_'+str(venueid)+ '_' +perform_time + '_' + title + ":データ数が０です。")

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
    
    fig.write_image("/home/shun/IconoijoiAggregationTools/media/"+str(venueid)+"_"+perform_time+"_"+title+".jpg",format='jpeg',scale=2,validate=False,engine='kaleido')
    return 

def piecreate(venueid,items,list,title,time):

    if(len(items)==0):
        logging.debug('<piecreate>'+time+'_'+str(venueid) + '_' + title + ":データ数が０です。")
        return
    value = []

    for i in range(0,len(list)):
        value.append(items.count(list[i]))

    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=list,
            values=value,
            title = title,
            sort = False,
            marker={'colors':['#98DBC6','#5BC8AC','#E6D72A','#F18D9E']},
               ),
    )

    fig.update_layout(
        showlegend = False,
        margin=dict(
            t=5,b=5,l=0,r=0
        ),
        font=dict(size=20),
        
    )

    fig.update_traces(
        textinfo='label+percent',
        hole = .4,
    )

    fig.write_image("/home/shun/IconoijoiAggregationTools/media/"+str(venueid)+'_'+title+".jpg",format='jpeg',scale=4,validate=False,engine='kaleido')

    return 



def int_row(row):
    int_rows = []
    try:    #列をint型に変換
        for i in range(len(row)):
            if (row[i] != ''):
                    int_rows.append(int(row[i] or 0))
    except:
        print("")
    return int_rows


def listcreate(rowlist,columnlist):
    list = {column:{row:0 for row in rowlist} for column in columnlist}
    return list

def textlistcreate(rowlist,columnlist):
    list = {column:{row:"" for row in rowlist} for column in columnlist}
    return list