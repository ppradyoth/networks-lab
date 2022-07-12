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