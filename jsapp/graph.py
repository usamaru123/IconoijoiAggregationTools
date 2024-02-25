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
    int_sheets = []
    int_columns = []
    for i in range(len(columns)):
        int_columns.append(int(columns[i] or 0))

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

    sheetlist = {}
    for s in range(len(sheets)):
        if (sheets[s] != '')and(columns[s] != '')and(rows[s] != ''):
            row = rows[s]
            int_column = int_columns[s]
            blocklist[row][int_column] = int_sheets[s]
    sheetdf = pd.DataFrame(blocklist)
    sns.heatmap(sheetdf,square=True,cbar=False,cmap='rainbow',linewidths=0.5,vmax=4.0,vmin=-4.0)
    graph = Output_Graph()
    return graph

def listcreate():
    alphabets = ['A','B','C','D','E','F','G']
    list = {}

    for block_r in alphabets:
        list[block_r] = {}
        for i in range(1,10):
            list[block_r][i] = 0
    return list
    
