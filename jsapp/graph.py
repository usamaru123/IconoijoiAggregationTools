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
    plt.plot(x,y)
    graph = Output_Graph()
    return graph
