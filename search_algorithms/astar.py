import heapq
from utils import heuristic, reconstruct_path


def astar(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}

    g_score = {node: float('inf') for node in graph.get_nodes()}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph.get_nodes()}
    f_score[start] = heuristic(graph.coordinates, start, goal)

    nodes_explored = 0
    visited = set()

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return path, nodes_explored

        for neighbor, weight in graph.get_neighbors(current).items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(graph.coordinates, neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, nodes_explored