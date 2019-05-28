from draw_node import DrawNodes

START_NODE = 0
visited = []

cities = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G"}

graph = {
    0: [1, 2],
    1: [6, 5],
    2: [6],
    3: [2],
    4: [5, 3],
    5: [],
    6: [],
}

h = DrawNodes(graph, cities, "DFS ALGORITHM")




def dfs(wierzcholek):
    visited.append(wierzcholek)

    for x in graph[wierzcholek]:
        if x not in visited:
            h.draw_nodes(x)
            h.draw_edge(wierzcholek, x)
            dfs(x)




h.draw_nodes(START_NODE)  # start

dfs(0)