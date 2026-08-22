def greedy_coloring(graph):
    nodes = graph.get_nodes()
    color_result = {}

    for node in nodes:
        neighbor_colors = set()
        for neighbor in graph.get_neighbors(node):
            if neighbor in color_result:
                neighbor_colors.add(color_result[neighbor])

        color = 0
        while color in neighbor_colors:
            color += 1

        color_result[node] = color

    return color_result