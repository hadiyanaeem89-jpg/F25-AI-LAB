graph = {
     "A":["B","C"],
     "B":["D","E"],
     "C":["F"],
     "D":[],
     "E":["G"],
     "F":[],
     "G":[]
} 

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    
    if limit == 0:
        if graph [node]:
            return "CUTOFF", None
        return "FAILURE",None
    cutoff_found = False
    
    for child in graph[node]:
        if child not in path:
            status, result = dls (
                child, goal, limit - 1, path + [child])
            
            if status == "FOUND":
                return status, result
            
            if status == "CUTOFF":
                cutoff_found = True
    if cutoff_found:
        return "CUTOFF", None
    return "FAILURE", None

def iddfs (start, goal, max_depth):
    for limit in range (max_depth + 1):
        status, path = dls(start, goal, limit,[start])
        
        print("limit:",limit,"status:", status)
        
        if status == "FOUND":
            print("path", path)
            return path
    
iddfs("A","G",4)