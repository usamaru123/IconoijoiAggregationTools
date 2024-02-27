import plotly.graph_objects as go
import pandas as pd
import numpy as np


def HeatMap(rows,numbers,sheets):
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
    rowlist = []
    columnlist = ['A','B','C','D','E','F','G']

    for i in range(0,10):
        rowlist.append(i+1)

    blocklist = listcreate(rowlist,columnlist)
    ippanlist = listcreate(rowlist,columnlist)
    kamekolist = listcreate(rowlist,columnlist)
    joseilist = listcreate(rowlist,columnlist)
    chakusekilist = listcreate(rowlist,columnlist)
    points = listcreate(rowlist,columnlist)
    text = listcreate(rowlist,columnlist)

    int_sheets = []
    int_columns = []
    int_rows = []





    sheetlist = [[0 for h in range(6)] for w in range(10)]

    #列と行をint型に変換
    for i in range(len(sheets)):
        if (sheets[i] != '')and(columns[i] != '')and(rows[i] != ''):        
                int_columns.append(int(columns[i] or 0))
                int_rows.append(rows[i])



    #座席種別ごとのリストに集計
    for i in range(len(int_rows)):
        if (sheets[i] != '')and(columns[i] != '')and(rows[i] != ''):

            int_column = int_columns[i]
            row = int_rows[i]

            ippan = ippanlist[int_column][row]
            kameko = kamekolist[int_column][row]
            josei = joseilist[int_column][row]
            chakuseki = chakusekilist[int_column][row]
            
            if sheets[i] == '一般席':
                ippan += 1
            elif sheets[i] == 'カメコエリア席':
                kameko += 1
            elif sheets[i] == '女性エリア席':
                josei += 1
            elif sheets[i] == '着席指定席':
                chakuseki += 1

    #すべてのリストでフィールドを参照し，一番集計数が多い座席種別をblocksheetに代入する
    for int_columns in range(len(int_columns)):
        for rows in range(len()):
            comparesheet = [ippan,kameko,josei,chakuseki]
            maxsheet = max(comparesheet.values())

    sheetdf = pd.DataFrame(kamekolist)
    textdf = pd.DataFrame(text)
    
    fig = go.Figure()
    fig.add_trace(go.Heatmap(
        x=sheetdf.columns,
        y=sheetdf.index,
        z=np.array(sheetdf),
        colorscale='Spectral',
        ))
    graph = fig.to_html(include_plotlyjs=False)
    return graph
 

def listcreate(rowlist,columnlist):
    list = {}
   

    for block_c in rowlist:
        list[block_c] = {}
        for block_r in columnlist:
            list[block_c][block_r] = 0
    return list
    
def sheetratio(sheets):
    sheetlist = ['一般席','カメコエリア席','女性エリア席','着席指定席']
    sheet_count = {} 
    colorlist = ["pink", "yellow", "skyblue", "orange"]

    general = sheets.count('一般席')
    camera = sheets.count('カメコエリア席')
    lady = sheets.count('女性エリア席')
    sit = sheets.count('着席指定席')
    
    valsheetlist = [general,camera,lady,sit]
    
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=sheetlist,values=valsheetlist))
    fig.show()
    graph = fig.to_html(include_plotlyjs=False)
    return graph