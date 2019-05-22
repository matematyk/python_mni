import networkx as nx
import matplotlib.pyplot as plt

plt.ion() #interactive mode on
# inne przykĹady na tworzenie grafu
H=nx.DiGraph()
#H.add_path([0,1,2,3,4])
H.add_edges_from(
    [(0, 1),
     (0, 2),
     (3, 2),
     (4, 3),
     (4, 5),
     (1, 6),
     (1, 5),
     (2, 6)])

cities = {0:"A",1:"B", 2:"C",3:"D", 4:"F", 5:"G", 6: "H"}

print("Nodes of graph: ")
print(H.nodes())
print("Edges of graph: ")
print(H.edges())


fig = plt.figure(1,figsize=(8,8))
ax = fig.add_axes((0,0,1,1))

#pos = nx.drawing.nx_agraph.graphviz_layout(H)
pos = nx.drawing.layout.planar_layout(H)

txt=fig.text(.05,.9,'DzieĹ dobry',fontsize=15)

for n in H:
    H.node[n]['draw'] = nx.draw_networkx_nodes(H,pos,nodelist=[n], node_size=200,alpha=0.5,node_color='k')
for u,v in H.edges():
    H[u][v]['draw']=nx.draw_networkx_edges(H,pos,edgelist=[(u,v)],alpha=0.5,arrows=False,width=5)


posL={}
for n,p in pos.items():  # raise text positions
#    posL[n] = (p[0],p[1] + 7)    # for graphviz_layout
    posL[n] = (p[0],p[1]+0.03)  # for nx.drawing.layout.planar_layout
    
labdraw = nx.draw_networkx_labels(H,posL,cities)
                        
plt.show()

plt.pause(1)

def draw_nodes(node): 
    txt.set_text('Pierwszy wierzcholek')

H.node[0]['draw'].set_color('r')
H.node[0]['draw'].set_alpha(1.0)

plt.pause(1)


visited = []

def dfs(graph, node):
    global visited
    if node not in visited:
        H.node[2]['draw'].set_color('r')
        visited.append(node)
        for n in graph[node]:
            draw_nodes(n)
            dfs(graph, n)
            
def draw_nodes(node):
    plt.pause(3)
    index = cities[node]
    H.node[index]['draw'].set_color('r')
    H.node[index]['draw'].set_alpha(1.0)


plt.pause(1)
txt.set_text('Nowa krawedz')

H.add_edge(0, 2)
H[0][2]['draw']=nx.draw_networkx_edges(H,pos,edgelist=[(0, 2)],alpha=1.0,arrows=True,width=5)

plt.pause(1)


plt.pause(2)

