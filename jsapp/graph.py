import matplotlib.pyplot as plt
import base64
from io import BytesIO

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
    int_y = []
    for i in range(len(y)):
        int_y.append(int(y[i] or 0))
    plt.switch_backend("AGG")
    plt.figure(figsize=(10,5))
    plt.plot(x,int_y)
    graph = Output_Graph()
    return graph
