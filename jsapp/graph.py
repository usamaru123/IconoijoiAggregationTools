import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np


def Floor_HeatMap(rows,numbers,sheets):
    int_rows = []
    int_numbers = []
    int_sheets = []


    for r in range(len(rows)):
        int_rows.append(int(rows[r] or 0))

    for n in range(len(numbers)):
        int_numbers.append(int(numbers[n] or 0))

    for i in range(len(sheets)):
        if sheets[i] == '一般席':
            int_sheets.append(1)
        elif sheets[i] == 'カメコエリア席':
            int_sheets.append(2)
        elif sheets[i] == '女性エリア席':
            int_sheets.append(3)
        elif sheets[i] == '着席指定席':
            int_sheets.append(4)
        else :
            int_sheets.append(0)

    sheetlist = [[0 for h in range(1,max(int_numbers)+2)] for w in range(1,max(int_rows)+2)]
    for s in range(len(int_sheets)):
        if (int_sheets[s] != 0)and(int_numbers[s] != 0):
            row = int_rows[s]
            number = int_numbers[s]
            sheetlist[row][number] = int_sheets[s]

    fig = go.Figure()
    fig.add_trace(go.Heatmap(sheetlist))    
    graph = fig.to_html(include_plotlyjs=False)
    return graph


def Arena_HeatMap(rows,columns,sheets):
    columnlist = []
    rowlist = ['A','B','C','D','E','F','G','H']

    for i in range(0,9):
        columnlist.append(i+1)

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
    for column in int_columns:
        for row in int_rows:
            try:
                comparesheet = {
                    '一':ippanlist[column][row],
                    'カ':kamekolist[column][row],
                    '女':joseilist[column][row],
                    '着':chakusekilist[column][row]
                    }
                
                maxsheetval = max(comparesheet.values())
                maxsheet = max(comparesheet,key=comparesheet.get)
                if maxsheetval == 0:
                    points[column][row] = 0
                    textlist[column][row] = 0
                else:
                    if maxsheet == '一':
                        points[column][row] = -1.5
                    if maxsheet == 'カ':
                        points[column][row] = -0.8
                    if maxsheet == '女':
                        points[column][row] = 1
                    if maxsheet == '着':
                        points[column][row] = 1.5
                    textlist[column][row] = maxsheet
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
        subplot_titles=['青：一般　橙：女エリ　水色：カメコ　赤：着席','【一般席】','【カメコ席】','【女性エリア席】','【着席指定席】',],
        vertical_spacing = 0.1
        )


    fig.add_trace(
        go.Heatmap(
        z=sheetdf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        colorscale='Edge',   
        zmax = 2,
        zmin = -2,
        text=text,  # 追加するテキスト
        texttemplate="%{label}",  # ホバーに追加する文字
        textfont={"size": 20}
        ),row=1,col=1)
    
    fig.add_trace(
        go.Heatmap(
        z=ippandf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        colorscale='Tropic',   
        zmax = 1,
        zmin = -1,
        ),row=2,col=1)
    
    fig.add_trace(
        go.Heatmap(
        z=kamekodf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        
        colorscale='Tropic',   
        zmax = 1,
        zmin = -1,
        ),row=3,col=1)
   
    fig.add_trace(
        go.Heatmap(
        z=joseidf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        
        colorscale='Tropic',   
        zmax = 1,
        zmin = -1,
        ),row=4,col=1)
       
    fig.add_trace(
        go.Heatmap(
        z=chakusekidf.values.tolist(),
        x=sheetdf.columns.tolist(),
        y=sheetdf.index.tolist(),
        colorscale='Tropic',   
        zmax = 1,
        zmin = -1,
        ),row=5,col=1)
    
    fig.update_layout(
        height=1500,
        margin_l=0,
        margin_r=0,
        font_family='sans-seif',
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

    graph = fig.to_html(include_plotlyjs=False)
    return graph