import networkx as nx
import matplotlib.pyplot as plt

plt.ion()

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'),
     ('A', 'C'),
     ('D', 'B'),
     ('E', 'C'),
     ('E', 'F'),
     ('B', 'H'),
     ('B', 'G'),
     ('B', 'F'),
     ('C', 'G')])


graph1 = {
    'A': ['B', 'C'],
    'B': ['H', 'G', 'F'],
    'C': ['G'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': [],
    'G': [],
    'H': [],
}

visited = []


val_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
val_map_c = {'A': 0.75}

values = [val_map_c.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
print(values)

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrows=True)


plt.show()
plt.pause(1)

print("wykonal sie")
def draw_nodes(node):
    plt.pause(3)
    index = val_map[node]
    values[index] = 0.75
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=values, node_size=500)
draw_nodes('D')

def dfs(graph, node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            draw_nodes(n)
            dfs(graph, n)


dfs(graph1, 'A')


plt.pause(1)


plt.pause(100)
plt.show()
