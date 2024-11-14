from collections import defaultdict

class BF_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        '''Add edge from node u to node v'''
        self.graph[u].append(v)    




    def traverse(self, s):
        '''Traverse the graph and print all vertex'''

        # Start by marking all vertices as unvisited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark source vertex as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from the queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s.
            # If an adjacent hasn't been visited, mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



g = BF_Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


print("Breadth-First  Traversl (start from vertex2):")
g.traverse(2)
