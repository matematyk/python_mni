import networkx as nx
import matplotlib.pyplot as plt


"""
W tym kodzie rysujemy graf, zadajemy go jako słownik i etykietki,
 oraz tekst opisujący algorytm. 
"""
plt.ion()  # interactive mode on


class RysujGraf:
    """
        graf- słownik, etykietki, słownik, tekst np "BFS Algorytm"
    """
    def __init__(self, graf, etykietki, tekst):
        # przekazanie grafu
        self.G = nx.DiGraph(graf)
        # graf reprezentowany jako słownik
        self.graf = graf

        self.etykietki = etykietki

        # ustawienie tekstu algorytmu
        self.tekst = tekst
        # ustawienie własności obrazu
        self.fig = plt.figure(1, figsize=(6, 6))
        self.txt = self.fig.text(.01, .9, self.tekst, fontsize=15)
        self.poz = nx.drawing.layout.planar_layout(self.G)

        self._plt_figures()


    """
        Rysowanie wierzchołka
    """
    def narysuj_wierzcholek(self, wierzcholek):
        plt.pause(1)
        # rysowanie wierzchołka odwiedzanego
        self.G.node[wierzcholek]['draw'].set_color('b')
        self.G.node[wierzcholek]['draw'].set_alpha(0.5)
        # rysowanie krawędzi
        self.txt.set_text(self.etykietki[wierzcholek])
        plt.pause(1)

    """
        Rysowanie krawędzi
    """
    def narysuj_krawedz(self, x, y):
        nx.draw_networkx_edges(self.G, self.poz, edgelist=[(x, y)], alpha=0.5, arrows=True, width=5)
        plt.pause(2)

    def _plt_figures(self):
        self.fig.add_axes((0, 0, 1, 1))

        for n in self.G:
            self.G.node[n]['draw'] = nx.draw_networkx_nodes(self.G, self.poz, nodelist=[n], node_size=100, alpha=0.5, node_color='r')
        for u, v in self.G.edges():
            self.G[u][v]['draw'] = nx.draw_networkx_edges(self.G, self.poz, edgelist=[(u, v)], alpha=0.5, arrows=True, width=5)

        pos_l = {}
        for n, p in self.poz.items():  # raise text positions
            pos_l[n] = (p[0], p[1] + 0.03)  # for nx.drawing.layout.planar_layout

        nx.draw_networkx_labels(self.G, pos_l, self.etykietki)

        plt.show()
        plt.pause(1)


