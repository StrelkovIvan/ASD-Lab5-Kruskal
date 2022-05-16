# Python program for Bellman-Ford's single source

class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))


    def BellmanFord(self, src):

        # Step 1:
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2:
        for i in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print ("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)


g.BellmanFord(0)

