import matplotlib.pyplot as plt
import base64
from io import BytesIO
import japanize_matplotlib
import seaborn as sns
import pandas as pd

def Output_Graph():
    buffer = BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    img = buffer.getvalue()
    graph  =base64.b64encode(img)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    

def Plot_Graph(x,y):
 #   int_y = []
  #  for i in range(len(y)):
  #      int_y.append(int(y[i] or 0)
    plt.switch_backend("AGG")
    plt.figure(figsize=(20,10))
    plt.plot(x,y)
    graph = Output_Graph()
    return graph


def sheetratio(sheets):
    sheetlist = ['一般席','カメコエリア席','女性エリア席','着席指定席']
    sheet_count = {} 
    colorlist = ["pink", "yellow", "skyblue", "orange"]

    general = sheets.count('一般席')
    camera = sheets.count('カメコエリア席')
    lady = sheets.count('女性エリア席')
    sit = sheets.count('着席指定席')
    
    valsheetlist = [general,camera,lady,sit]
    
    for i in range(len(sheetlist)):
        sheet_count[sheetlist[i]] = valsheetlist[i]

    sheet_countdf = pd.DataFrame(sheet_count,index=[0])
    plt.pie(valsheetlist,
            labels=sheetlist,
            counterclock=True,
            autopct="%1.1f%%",
            colors=colorlist, 
            )
    plt.legend(prop = {"family" : "Meiryo"})
    graph = Output_Graph()
    return graph