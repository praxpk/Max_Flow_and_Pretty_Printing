from Graph import graph
from node import node
def main():
    #create common source vertex
    g1 = graph()
    source = node("s")
    g1.add_vertex(source)
    SO = node("so")
    g1.add_vertex(SO)
    SA = node("sa")
    g1.add_vertex(SA)
    SB = node("sb")
    g1.add_vertex(SB)
    SAB = node("sab")
    g1.add_vertex(SAB)
    DO = node("do")
    g1.add_vertex(DO)
    DA = node("da")
    g1.add_vertex(DA)
    DB = node("db")
    g1.add_vertex(DB)
    DAB = node("dab")
    g1.add_vertex(DAB)
    sink=node("si")
    g1.add_vertex(sink)
    g1.add_edge(source,SO,50)
    g1.add_edge(source,SA,36)
    g1.add_edge(source,SB,11)
    g1.add_edge(source,SAB,8)
    g1.add_edge(DO, sink, 45)
    g1.add_edge(DA, sink, 42)
    g1.add_edge(DB, sink, 8)
    g1.add_edge(DAB, sink, 3)
    g1.add_edge(SO,DO,float("inf"))
    g1.add_edge(SO, DA, float("inf"))
    g1.add_edge(SO, DB, float("inf"))
    g1.add_edge(SO, DAB, float("inf"))
    g1.add_edge(SA, DA, float("inf"))
    g1.add_edge(SA, DAB, float("inf"))
    g1.add_edge(SB, DB, float("inf"))
    g1.add_edge(SB, DAB, float("inf"))
    g1.add_edge(SAB, DAB, float("inf"))
    max_flow=g1.find_max_flow(source,sink)
    demand = g1.edges[(DO,sink)]+g1.edges[(DA,sink)]+g1.edges[(DB,sink)]+g1.edges[(DAB,sink)]
    print("MAX_FLOW = ",max_flow)
    print("Demand = ",demand)
    if(demand>max_flow):
        print("Max flow is lesser than demand. Hence, demand cannot be met.")
    else:
        print("Max flow is equal to or more than demand. Hence, demand can be met.")







if __name__ == '__main__':
    main()