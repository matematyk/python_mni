from rysuj_graf import RysujGraf
import collections

wierzcholek_startowy = 0


# etykiety wyswietlane
etykietki = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I"}

# graf lista
graf = {
    0: [1],
    1: [2, 3],
    2: [3],
    3: [4],
    5: [],
    6: [7, 8],
    7: [],
    8: [],
}
# Obiekt DrawNodes przyjmuje 3 parametry, graf, liste etykiet, oraz nazwe algorytmu
h = RysujGraf(graf, etykietki, "BFS ALGORYTM")

def bfs(graf, root):
    odwiedzone, queue = set(), collections.deque([root])
    while queue:
        wierzcholek = queue.popleft()
        for sasiad in graf[wierzcholek]:
            if sasiad not in odwiedzone:
                h.narysuj_wierzcholek(sasiad)
                h.narysuj_krawedz(wierzcholek, sasiad)
                odwiedzone.add(sasiad)
                queue.append(sasiad)


h.narysuj_wierzcholek(wierzcholek_startowy)
bfs(graf, wierzcholek_startowy)
