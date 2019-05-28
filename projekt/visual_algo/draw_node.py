import networkx as nx
import matplotlib.pyplot as plt

'''To jest modul do rysowanania grafu
Graf zadawny jest jako 
* przekazanie grafu jako listy sąsiedztwa
* jako slownik etykiet, konkretnych node,
* parametr tesktowy algorytmu 

'''


class DrawNodes:

    def __init__(self, graph, cities, text):
        plt.ion()  # interactive mode on
        self.H = nx.DiGraph(graph)
        # przekazanie grafu jako listy sąsiedztwa
        self.graph = graph
        # ustawienie tekstu algorytmu
        self.text = text
        self.cities = cities
        # Zdefiniowanie figure
        self.fig = plt.figure(1, figsize=(8, 8))
        self.txt = self.fig.text(.05, .9, self.text, fontsize=15)
        self.pos = nx.drawing.layout.planar_layout(self.H)
        self.plt_figures()

    def plt_figures(self):
        self.fig.add_axes((0, 0, 1, 1))
        self.txt = self.fig.text(.05, .9, self.text, fontsize=15)

        for n in self.H:
            self.H.node[n]['draw'] = nx.draw_networkx_nodes(self.H, self.pos, nodelist=[n], node_size=200, alpha=0.5, node_color='k')
        for u, v in self.H.edges():
            self.H[u][v]['draw'] = nx.draw_networkx_edges(self.H, self.pos, edgelist=[(u, v)], alpha=0.5, arrows=True, width=5)

        pos_l = {}
        for n, p in self.pos.items():  # raise text positions
            pos_l[n] = (p[0], p[1] + 0.03)  # for nx.drawing.layout.planar_layout

        nx.draw_networkx_labels(self.H, pos_l, self.cities)

        plt.show()
        plt.pause(1)

    def draw_nodes(self, node):
        plt.pause(1)
        # rysowanie wierzchołka odwiedzanego
        self.H.node[node]['draw'].set_color('r')
        self.H.node[node]['draw'].set_alpha(1.0)
        # rysowanie krawędzi
        self.txt.set_text(self.cities[node])
        plt.pause(1)

    def draw_edge(self, x, y):
        nx.draw_networkx_edges(self.H, self.pos, edgelist=[(x, y)], alpha=1.0, arrows=True, width=5)
        plt.pause(3)

    def pl_show(self):
        plt.show()


