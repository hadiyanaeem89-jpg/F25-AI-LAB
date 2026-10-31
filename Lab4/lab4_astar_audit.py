import heapq

graph = {
    "S":[("A",1),("B",4)],
    "A": [("C", 2)],
    "B":[("G" , 5)],
    "c":[("G", 3)],
    "G":[]
}

heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G":0
}

def search(start, goal, h):
    pq =[(h[start], 0 , start, [start])]
    best = {start:0}
    processed = []
    
    
    while pq:
        f, g, node, path = heapq.heappop(pq)
        
        if g != best[node]:
            continue
        processed.append(node)
        print("processed", node, "g", g, "h", h[node], "f", f)
        
        
        
        if node == goal:
            return path, g, processed
        
        for child, weight in graph[node]:
            new_g = g + weight
        
        if new_g < best.get(child, float("inf")):
            best[child] = new_g
            new_f = new_g + h[child]
            
            heapq.heappush( pq, (new_f, new_g, child, path + [child]))
            return None, float ("inf"), processed
        
        
print("A* search")
astar_path, astar_cost, astar_order = search("S", "G",heuristic)

print("A* path", astar_path)
print("A* cost", astar_cost)
print("A*processed", astar_order)

print("\n UCS search")
zero_heuristic ={node: 0 for node in graph}

ucs_path, ucs_cost, ucs_order = search("S", "G", zero_heuristic)


print("UCS path",ucs_path)
print("UCS cost", ucs_order)
        