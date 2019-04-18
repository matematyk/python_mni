visited = []

graf = {0: {1, 2}, 
		1: {3, 2, 0}, 
		2: {4, 1, 0}, 
		3: {1, 4}, 
		4: {3,2,5}, 
		5: {6,4},
		6: {5}
    }

def dfs_wierzcholek(wierzcholek): 
    visited.append(wierzcholek) 
    print(wierzcholek)
    
    for x in graf[wierzcholek]:
        if x not in visited:
            dfs_wierzcholek(x)
dfs_wierzcholek(0)

	
