#graph=[(1,2),(2,3),(3,4),(4,5),(1,3),(2,4),(3,5)]
#vertexset=set()
#for edge in graph:
#    print(edge)
#   vertexset.add(edge[0])
#    vertexset.add(edge[1])
#print("no of vertices=",len(vertexset))
#print("no of edges=",len(graph))
def distance(e):
    return e[2]
graph=[(1,2,5),(2,3,4),(3,4,10),(4,5,6),(1,3,9),(2,4,6),(3,5,8)]
vertexset=set()
td=0
for edge in graph:
    print(edge)
    vertexset.add(edge[0])
    vertexset.add(edge[1])
    td=td+edge[2]
print("total distance of graph is",td)
print("no of vertices=",len(vertexset))
print("no of edges=",len(graph))
graph.sort(key=distance)
print("sorted graph based on distance")
print(graph)
    



    
