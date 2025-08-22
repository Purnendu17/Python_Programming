from collections import deque

def bfs(graph, source):
    visited = set()
    queue = deque([source])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))  # Add next val to the queue

    return result

# Taking input from the user
def input_graph():
    graph = {}
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    print("Enter edges in the format 'src dest':")
    for _ in range(E):
        src, dest = map(int, input().split())
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)  # Directed graph

    return graph

# Main execution
graph = input_graph()
source = int(input("Enter the starting vertex: "))
print("BFS Traversal Order:", bfs(graph, source))