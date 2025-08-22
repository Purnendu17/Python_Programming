def dfs(graph, source, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(source)
    result.append(source)

    for neighbor in graph.get(source, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

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
print("DFS Traversal Order:", dfs(graph, source))