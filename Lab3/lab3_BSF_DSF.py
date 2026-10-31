from collections import deque
 
graph = {
     "A":["B","C"],
     "B":["D","E"],
     "C":["F"],
     "D":[],
     "E":["G"],
     "F":[],
     "G":[]
} 
    
def bsf (start , goal):
    queue = deque ([(start,[start])])
    seen ={start}
    order =[]
    
    while queue:
        node, path = queue.popleft()
        order.append (node)
        if node == goal:
            return path , order
        
        for n in graph [node]:
            if n not in seen:
                seen.add(n)
                queue.append((n,path + [n]))
        
        
def dfs(start, goal):
    stack = [(start, [start])]
    seen = set ()
    order = []
    while stack:
        node, path = stack.pop()
        
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        
        if node == goal:
            return path, order
        for n in reversed(graph[node]):
            stack.append((n, path + [n]))
bfs_path, bfs_order = bsf("A", "G")
dfs_path, dfs_order = dfs("A", "G")

print("BFS visit order" ,bfs_order)
print("BFS path", bfs_order)            

print("BFS visit order", bfs_order)
print("BFS path", bfs_order)    
                