import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px
from plotly.offline import plot
import pandas as pd
import numpy as np


def Floor_HeatMap(rows,numbers):
   return 

def Arena_HeatMap(rows,columns,sheets,rowmax,columnmax):
    if (rows is None):
        return
        
    columnlist = []
    rowlist = []

    row = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

    for i in range(0,columnmax):
        columnlist.append(i+1)

    for i in range(0,rowmax):
        rowlist.append(row[i])

    blocklist = listcreate(rowlist,columnlist)
    ippanlist = listcreate(rowlist,columnlist)
    kamekolist = listcreate(rowlist,columnlist)
    joseilist = listcreate(rowlist,columnlist)
    chakusekilist = listcreate(rowlist,columnlist)
    points = listcreate(rowlist,columnlist)
    textlist = listcreate(rowlist,columnlist)

    int_sheets = []
    int_columns = []
    int_rows = []

    try:
    #列と行をint型に変換
        for i in range(len(sheets)):
            if (sheets[i] != '')and(columns[i] != '')and(rows[i] != ''):        
                    int_columns.append(int(columns[i] or 0))
                    int_rows.append(rows[i])
    except:
        print("")


    #座席種別ごとのリストに集計
    for i in range(len(int_rows)):

        column = int_columns[i]
        row = int_rows[i]
        try:
            if sheets[i] == '一般席':
                ippanlist[column][row] += 1
            elif sheets[i] == 'カメコエリア席':
                kamekolist[column][row] += 1
            elif sheets[i] == '女性エリア席':
                joseilist[column][row] += 1
            elif sheets[i] == '着席指定席':
                chakusekilist[column][row] += 1
            blocklist[column][row] +=1
        except:
            print("座席がリスト外")

    #すべてのリストでフィールドを参照し，一番集計数が多い座席種別をblocksheetに代入する
    for column in range(len(int_columns)):
        for row in range(len(int_rows)):
            try:
                comparesheet = {
                    '一':ippanlist[column][row],
                    'カ':kamekolist[column][row],
                    '女':joseilist[column][row],
                    '着':chakusekilist[column][row]
                    }
                
                maxsheetval = max(comparesheet.values())
                maxsheet = max(comparesheet,key=comparesheet.get)
                if (maxsheetval != 0):
                    if maxsheet == '一':
                        points[column][row] = -1.5
                    if maxsheet == 'カ':
                        points[column][row] = -0.8
                    if maxsheet == '女':
                        points[column][row] = 1
                    if maxsheet == '着':
                        points[column][row] = 1.5
                    textlist[column][row] = 'a'

                else:
                    textlist[column][row] = "4"
            except:
                print("")


    sheetdf = pd.DataFrame(points)
    ippandf = pd.DataFrame(ippanlist)
    kamekodf = pd.DataFrame(kamekolist)
    joseidf = pd.DataFrame(joseilist)
    chakusekidf = pd.DataFrame(chakusekilist)
    textdf = pd.DataFrame(textlist)
    text = textdf.values.tolist()


    fig = make_subplots(
        rows=5,
        cols=1,
        vertical_spacing = 0.1,
        subplot_titles=['ブロックの中で一番多かった座席種別を表示','一般席','カメコエリア席','女性エリア席','着席指定席'],
        )


    fig.add_trace(
        go.Heatmap(
        z=sheetdf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        text = text,
        colorscale='Edge',   
        zmax = 2,
        zmin = -2,
        xgap=2,
        ygap=2,
        texttemplate="%{text}",
        ),row=1,col=1)
    
    fig.add_trace(
        go.Heatmap(
        z=ippandf.values.tolist(),
        x=ippandf.columns.tolist(),
        y=ippandf.index.tolist(),
        colorscale='Blues',   
        zmax = 10,
        zmin = 0,
        xgap=2,
        ygap=2,
        texttemplate="%{z}",
        ),row=2,col=1)
    
    fig.add_trace(
        go.Heatmap(
        z=kamekodf.values.tolist(),
        x=kamekodf.columns.tolist(),
        y=kamekodf.index.tolist(),
        colorscale='BuGn',   
        zmax = 10,
        zmin = 0,
        xgap=2,
        ygap=2,
        texttemplate="%{z}",
        ),row=3,col=1)
   
    fig.add_trace(
        go.Heatmap(
        z=joseidf.values.tolist(),
        x=joseidf.columns.tolist(),
        y=joseidf.index.tolist(),
        colorscale='PuRd',   
        zmax = 10,
        zmin = 0,
        xgap=2,
        ygap=2,
        texttemplate="%{z}",
        ),row=4,col=1)
       
    fig.add_trace(
        go.Heatmap(
        z=chakusekidf.values.tolist(),
        x=chakusekidf.columns.tolist(),
        y=chakusekidf.index.tolist(),
        colorscale='Purples',
        zmax = 10,
        zmin = 0,
        xgap=2,
        ygap=2,
        texttemplate="%{z}",
        ),row=5,col=1)
    
    fig.update_layout(
        height=1500,
        margin_l=0,
        margin_r=0,
    )
    fig.update_traces(showscale=False)
    fig.update_yaxes(autorange='reversed',dtick=1)
    fig.update_xaxes(dtick=1)

    graph = fig.to_html(include_plotlyjs=False)
    return graph
 

def listcreate(rowlist,columnlist):
    list = {column:{row:0 for row in rowlist} for column in columnlist}
    return list
    
def sheetratio(sheets):
    sheetlist = ['一般席','カメコエリア席','女性エリア席','着席指定席'] 
    general = sheets.count('一般席')
    camera = sheets.count('カメコエリア席')
    lady = sheets.count('女性エリア席')
    sit = sheets.count('着席指定席')
    
    valsheetlist = [general,camera,lady,sit]

    return piecreate(sheetlist,valsheetlist)


def piecreate(label,value):

    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=label,
            values=value,
            title = '座席種別',
            sort = False,
            marker={'colors':['#98DBC6','#5BC8AC','#E6D72A','#F18D9E']},
               ),
    )

    fig.update_layout(
        showlegend = False,
        margin=dict(
            t=5,b=5,l=0,r=0
        ),
    )

    fig.update_traces(
        textinfo='label+percent',
        hole = .4,
    )

    graph = plot(fig, output_type='div', include_plotlyjs=True)
    return graph