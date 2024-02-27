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
    blocklist = listcreate()
    ippanlist = listcreate()
    kamekolist = listcreate()
    joseilist = listcreate()
    chakusekilist = listcreate()
    points = listcreate()
    text = listcreate()

    int_sheets = []
    int_columns = []
    int_rows = []

    alphabets = ['A','B','C','D','E','F','G']

    sheetlist = [[0 for h in range(6)] for w in range(10)]

    
    for i in range(len(sheets)):
        if (sheets[i] != '')and(columns[i] != '')and(rows[i] != ''):        
                int_columns.append(int(columns[i] or 0))
                int_rows.append(rows[i])


    for i in range(len(int_rows)):
        if (sheets[i] != '')and(columns[i] != '')and(rows[i] != ''):
                int_column = int_columns[i]
                row = int_rows[i]

                if sheets[i] == '一般席':
                    ippanlist[int_column][row] += 1
                    int_sheets.append(1)
                elif sheets[i] == 'カメコエリア席':
                    int_sheets.append(2)
                    kamekolist[int_column][row] += 1
                elif sheets[i] == '女性エリア席':
                    int_sheets.append(3)
                    joseilist[int_column][row] += 1
                elif sheets[i] == '着席指定席':
                    int_sheets.append(4)
                    chakusekilist[int_column][row] += 1
                else :
                    int_sheets.append(0)



    sheetdf = pd.DataFrame(points)
    textdf = pd.DataFrame(text)
    
    fig = go.Figure()
    fig.add_trace(go.Heatmap(
        x=sheetdf.columns,
        y=sheetdf.index,
        z=np.array(ippanlist)
        ))
    graph = fig.to_html(include_plotlyjs=False)
    return graph
 

def listcreate():
    alphabets = ['A','B','C','D','E','F','G']
    list = {}
   

    for i in range(1,10):
        list[i] = {}
        for block_r in alphabets:
            list[i][block_r] = 0
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