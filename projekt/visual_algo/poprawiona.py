import networkx as nx
import matplotlib.pyplot as plt

'''To jest modul do rysowanania grafu'''


class DrawNodes:

    def __init__(self, graph, cities, text):
        plt.ion()  # interactive mode on
        self.H = nx.DiGraph(graph)
        self.graph = graph
        self.text = text
        self.cities = cities
        self.fig = plt.figure(1, figsize=(8, 8))
        self.txt = self.fig.text(.05, .9, self.text, fontsize=15)
        self.plt_figures()

    def plt_figures(self):
        ax = self.fig.add_axes((0, 0, 1, 1))
        pos = nx.drawing.layout.planar_layout(self.H)
        self.txt = self.fig.text(.05, .9, self.text, fontsize=15)

        for n in self.H:
            self.H.node[n]['draw'] = nx.draw_networkx_nodes(self.H, pos, nodelist=[n], node_size=200, alpha=0.5, node_color='k')
        for u, v in self.H.edges():
            self.H[u][v]['draw'] = nx.draw_networkx_edges(self.H, pos, edgelist=[(u, v)], alpha=0.5, arrows=True, width=5)

        pos_l = {}
        for n, p in pos.items():  # raise text positions
            pos_l[n] = (p[0], p[1] + 0.03)  # for nx.drawing.layout.planar_layout

        nx.draw_networkx_labels(self.H, pos_l, self.cities)

        plt.show()
        plt.pause(1)

    def draw_nodes(self, node):
        plt.pause(1)
        self.H.node[node]['draw'].set_color('r')
        self.H.node[node]['draw'].set_alpha(1.0)
        #self.txt.set_text(self.cities[node])
        plt.pause(1)

    def pl_show(self):
        plt.show()


