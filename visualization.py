import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(graph, path=None, coloring=None, title="Smart City Map"):
    G = nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for node, neighbors in graph.adjacency_list.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = graph.coordinates

    plt.figure(figsize=(10, 7))

    if coloring:
        palette = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#95E1D3", "#A28089", "#6C5B7B"]
        node_colors = [palette[coloring[node] % len(palette)] for node in G.nodes()]
    else:
        node_colors = "#87CEEB"

    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=1500, font_size=8, font_weight="bold", edge_color="gray")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange", node_size=1500)

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()