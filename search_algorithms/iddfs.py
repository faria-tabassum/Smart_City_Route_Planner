def dls(graph, current, goal, limit, visited, path, nodes_explored):
    nodes_explored[0] += 1
    if current == goal:
        return path

    if limit <= 0:
        return None

    visited.add(current)
    for neighbor in graph.get_neighbors(current):
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, limit - 1, visited, path + [neighbor], nodes_explored)
            if result is not None:
                return result
    visited.remove(current)
    return None


def iddfs(graph, start, goal, max_depth=20):
    nodes_explored = [0]
    for depth in range(max_depth + 1):
        visited = set()
        result = dls(graph, start, goal, depth, visited, [start], nodes_explored)
        if result is not None:
            return result, nodes_explored[0]
    return None, nodes_explored[0]