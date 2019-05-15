import networkx as nx
import matplotlib.pyplot as plt

plt.ion()  # interactive mode on
# inne  na tworzenie grafu
H = nx.path_graph(5)
cities = {0: "Toronto", 1: "London", 2: "Berlin", 3: "New York", 4: "Warszawa"}

print("Nodes of graph: ")
print(H.nodes())
print("Edges of graph: ")
print(H.edges())

fig = plt.figure(1, figsize=(8, 8))
ax = fig.add_axes((0, 0, 1, 1))

pos = nx.drawing.nx_agraph.graphviz_layout(H)
# pos = nx.drawing.layout.planar_layout(H)

txt = fig.text(.05, .9, ' dobry', fontsize=15)

for n in H:
    H.node[n]['draw'] = nx.draw_networkx_nodes(H, pos, nodelist=[n], node_size=200, alpha=0.5, node_color='k')
for u, v in H.edges():
    H[u][v]['draw'] = nx.draw_networkx_edges(H, pos, edgelist=[(u, v)], alpha=0.5, arrows=False, width=5)

posL = {}
for n, p in pos.items():  # raise text positions
    posL[n] = (p[0], p[1] + 7)  # for graphviz_layout
#    posL[n] = (p[0],p[1]+0.03)  # for nx.drawing.layout.planar_layout

labdraw = nx.draw_networkx_labels(H, posL, cities)

plt.show()

plt.pause(1)

txt.set_text('Jeden ')

H.node[0]['draw'].set_color('r')
H.node[0]['draw'].set_alpha(1.0)

plt.pause(1)
txt.set_text('Drugi ')

H.node[2]['draw'].set_color('r')
H.node[2]['draw'].set_alpha(1.0)

plt.pause(1)
txt.set_text('Nowa ')

H.add_edge(0, 2)
H[0][2]['draw'] = nx.draw_networkx_edges(H, pos, edgelist=[(0, 2)], alpha=1.0, arrows=True, width=5)

plt.pause(1)
txt.set_text('Drugi graf')

# HH=nx.cycle_graph(4)

# plt.figure(2)
# nx.draw(HH)

plt.pause(1)
# plt.figure(1) #Niepotrzebne, bo txt ma  ustawiony figure
txt.set_text('Zmiana etykiety')

labdraw[2].set_text("Berlin ZOO")


