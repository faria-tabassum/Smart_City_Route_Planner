from collections import deque


def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    visited.add(start)
    nodes_explored = 0

    if start == goal:
        return [start], nodes_explored

    while queue:
        path = queue.popleft()
        current = path[-1]
        nodes_explored += 1

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path, nodes_explored
                visited.add(neighbor)
                queue.append(new_path)

    return None, nodes_explored