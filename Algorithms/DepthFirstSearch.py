
# Given Graph
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 


from collections import defaultdict

class DepthFirstSearch:
    #To store in dictionary
    def __init__(self):
        self.graph = defaultdict(list)
    
    #Add Element
    def addElements(self,a,b):
        self.graph[a].append(b)

    #Traversing the current node and print
    def traverse(self,b,visited):
        visited.add(b)
        print(b)

        for i in self.graph[b]:
            if i not in visited:
                self.traverse(i,visited)
    
    #Store visited elements
    def dfs(self):
        visited= set()

        for j in self.graph:
            if j is not visited:
                self.traverse(j,visited)

g = DepthFirstSearch()
g.addElements(0,1)
g.addElements(0,2)     
g.addElements(1,2) 
g.addElements(2,0) 
g.addElements(2,3) 
g.addElements(3,3) 
g.dfs()
