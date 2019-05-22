def dfs(graph, node, draw_nodes):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            draw_nodes(n)
            dfs(graph, n)