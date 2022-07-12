class Graph:

    def __init__(self, vertices):
        self.V = vertices   
        self.graph = []     

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(i,"\t\t\t\t",dist[i])

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0
        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

   
        self.print_solution(dist)


v=int(input("Please enter the number of vertices:\n"))
g = Graph(v)
e=int(input("Please enter the number of edges:\n"))
src=int(input("Please enter the source vertex number (0-v):\n"))
for i in range(e):
    s,d,w=input("Please enter edge number (src , des , weight) "+str(i+1)+" : ").split()
    s=int(s)
    d=int(d)
    w=int(w)
    g.addEdge(s,d,w)
g.bellman_ford(src)

# Please enter the number of vertices:
# 6
# Please enter the number of edges:
# 9
# Please enter the source vertex number (0-v):
# 0
# Please enter edge number (src , des , weight) 1 : 0 1 2
# Please enter edge number (src , des , weight) 2 : 0 2 4
# Please enter edge number (src , des , weight) 3 : 1 2 1
# Please enter edge number (src , des , weight) 4 : 1 4 2
# Please enter edge number (src , des , weight) 5 : 1 3 -4
# Please enter edge number (src , des , weight) 6 : 2 4 3
# Please enter edge number (src , des , weight) 7 : 4 3 3
# Please enter edge number (src , des , weight) 8 : 4 5 2
# Please enter edge number (src , des , weight) 9 : 3 5 2
# Vertex Distance from Source
# 0                                0
# 1                                2
# 2                                3
# 3                                -2
# 4                                4
# 5                                0