import matplotlib.pyplot as plt
import networkx as nx


def _prepare_axes(graph, path=None, coloring=None, title="Smart City Map"):
    """Shared drawing logic used by both the CLI popup and the GUI embed."""
    G = nx.Graph()

    for node in graph.get_nodes():
        G.add_node(node)

    for node, neighbors in graph.adjacency_list.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = graph.coordinates

    fig, ax = plt.subplots(figsize=(8, 6))

    if coloring:
        palette = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#95E1D3", "#A28089", "#6C5B7B"]
        node_colors = [palette[coloring[node] % len(palette)] for node in G.nodes()]
    else:
        node_colors = "#87CEEB"

    nx.draw(G, pos, ax=ax, with_labels=True, node_color=node_colors,
            node_size=1500, font_size=10, font_weight="bold", font_color="black",
            edge_color="gray")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, ax=ax)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange", node_size=1500, ax=ax)
        nx.draw_networkx_labels(G, pos, labels={n: n for n in path},
                                 font_size=10, font_weight="bold", font_color="black", ax=ax)

    ax.set_title(title)
    ax.axis("off")
    fig.tight_layout()
    return fig


def draw_graph(graph, path=None, coloring=None, title="Smart City Map"):
    """CLI version - opens a popup window (used by main.py)."""
    _prepare_axes(graph, path=path, coloring=coloring, title=title)
    plt.show()


def build_figure(graph, path=None, coloring=None, title="Smart City Map"):
    """GUI version - returns the figure so it can be embedded in a tkinter window."""
    return _prepare_axes(graph, path=path, coloring=coloring, title=title)
