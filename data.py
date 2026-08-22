from graph import Graph


def build_city_graph():
    g = Graph()

    g.add_node("Hospital", 0, 0)
    g.add_node("Mall", 4, 0)
    g.add_node("School", 0, 3)
    g.add_node("Junction_1", 4, 3)
    g.add_node("Park", 8, 3)
    g.add_node("Market", 8, 0)
    g.add_node("Stadium", 12, 0)
    g.add_node("Library", 12, 3)
    g.add_node("Bank", 4, 6)
    g.add_node("Junction_2", 8, 6)
    g.add_node("Airport", 12, 6)
    g.add_node("University", 0, 6)
    g.add_node("Museum", 16, 3)
    g.add_node("Zoo", 16, 6)
    g.add_node("Station", 16, 0)

    g.add_edge("Hospital", "Mall", 4)
    g.add_edge("Hospital", "School", 3)
    g.add_edge("Mall", "Junction_1", 3)
    g.add_edge("School", "Junction_1", 4)
    g.add_edge("Junction_1", "Park", 4)
    g.add_edge("Junction_1", "Bank", 3)
    g.add_edge("Park", "Market", 3)
    g.add_edge("Market", "Stadium", 4)
    g.add_edge("Park", "Library", 3)
    g.add_edge("Stadium", "Library", 3)
    g.add_edge("Library", "Airport", 3)
    g.add_edge("Stadium", "Museum", 4)
    g.add_edge("Museum", "Station", 4)
    g.add_edge("Airport", "Zoo", 3)
    g.add_edge("Museum", "Zoo", 3)
    g.add_edge("Zoo", "Station", 4)
    g.add_edge("Bank", "Junction_2", 4)
    g.add_edge("Junction_2", "Airport", 4)
    g.add_edge("University", "Bank", 3)
    g.add_edge("University", "School", 3)

    return g