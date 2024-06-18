from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
print("BFS starting from node 2:")
graph.bfs(2)