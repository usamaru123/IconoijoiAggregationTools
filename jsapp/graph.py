import matplotlib.pyplot as plt
import base64
from io import BytesIO
import japanize_matplotlib

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
  #      int_y.append(int(y[i] or 0))
    plt.switch_backend("AGG")
    plt.figure(figsize=(10,5))
    plt.plot(x,y)
    plt.legend(prop={'family':'MS Gothic'})
    graph = Output_Graph()
    return graph


def HeatMap(x,sheets):
    int_sheet = []
    for i in range(len(sheets)):
        if sheets[i] == '一般席':
            int_sheet.append(1)
        elif sheets[i] == 'カメコエリア席':
            int_sheet.append(2)
        elif sheets[i] == '女性エリア席':
            int_sheet.append(3)
        elif sheets[i] == '着席指定席':
            int_sheet.append(2)
        else :
            int_sheet.append(0)
        print (sheets[i])

    sheetlist = [[0 for h in range(50)] for w in range(90)]
    sheetlist[1,1] = 10
    fig,ax = plt.subplots()
    im = ax.imshow(sheetlist)
    graph = Output_Graph()
    return graph