import matplotlib.pyplot as plt
import base64
from io import BytesIO
import japanize_matplotlib
import seaborn as sns
import pandas as pd
sns.set()

def Output_Graph():
    buffer = BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    img = buffer.getvalue()
    graph  =base64.b64encode(img)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph

def Plot_Graph(x,y):
 #   int_y = []
  #  for i in range(len(y)):
  #      int_y.append(int(y[i] or 0)
    plt.switch_backend("AGG")
    plt.figure(figsize=(20,10))
    plt.plot(x,y)
    plt.legend(prop={'family':'MS Gothic'})
    graph = Output_Graph()
    return graph


def HeatMap1(rows,numbers,sheets):
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
        print (sheets[i])

    sheetlist = [[0 for h in range(1,max(int_numbers)+2)] for w in range(1,max(int_rows)+2)]
    for s in range(len(int_sheets)):
        if (int_sheets[s] != 0)and(int_numbers[s] != 0):
            row = int_rows[s]
            number = int_numbers[s]
            sheetlist[row][number] = int_sheets[s]
            
    sns.heatmap(sheetlist,square=True,cbar=False,)
    graph = Output_Graph()
    return graph


def Arena_HeatMap(rows,columns,sheets):
    blocklist = listcreate()
    ippanlist = listcreate()
    kamekolist = listcreate()
    joseilist = listcreate()
    chakusekilist = listcreate()
    points = listcreate()

    int_sheets = []
    int_columns = []
    int_rows = []

    alphabets = ['A','B','C','D','E','F','G']

    
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

    for i in range(len(blocklist)):
        for j in alphabets:
            points[i][j] = ippanlist[i][j]+kamekolist[i][j]+joseilist[i][j]+chakusekilist[i][j]

    sheetdf = pd.DataFrame(points)
    sns.heatmap(sheetdf,square=True,cbar=False,cmap='nipy_spectral_r',linewidths=0.5,vmax=5.0,vmin=0)
    plt.yticks(rotation=0)
    graph = Output_Graph()
    return graph

def listcreate():
    alphabets = ['A','B','C','D','E','F','G']
    list = {}

    for i in range(1,10):
        list[i] = {}
        for block_r in alphabets:
            list[i][block_r] = 0
    return list
    
