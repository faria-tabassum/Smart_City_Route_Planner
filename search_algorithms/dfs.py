def dfs(graph, start, goal):
    visited = set()
    nodes_explored = [0]

    def dfs_recursive(current, path):
        visited.add(current)
        nodes_explored[0] += 1

        if current == goal:
            return path

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                result = dfs_recursive(neighbor, path + [neighbor])
                if result is not None:
                    return result

        return None

    result_path = dfs_recursive(start, [start])
    return result_path, nodes_explored[0]