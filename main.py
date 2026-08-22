from data import build_city_graph
from search_algorithms.bfs import bfs
from search_algorithms.dfs import dfs
from search_algorithms.iddfs import iddfs
from search_algorithms.astar import astar
from coloring.graph_coloring import greedy_coloring
from utils import measure_time
from visualization import draw_graph


def print_menu():
    print("\n===== SMART CITY ROUTE PLANNER =====")
    print("1. Find Route using BFS")
    print("2. Find Route using DFS")
    print("3. Find Route using IDDFS")
    print("4. Find Route using A* Search")
    print("5. Compare All Algorithms")
    print("6. Traffic Signal Coloring")
    print("7. Show City Map")
    print("8. Exit")


def print_path_result(algo_name, path, nodes_explored, elapsed_ms):
    if path is None:
        print(f"\n[{algo_name}] No path found.")
        return
    print(f"\n[{algo_name}]")
    print("Path: " + " -> ".join(path))
    print(f"Total Stops: {len(path) - 1}")
    print(f"Nodes Explored: {nodes_explored}")
    print(f"Time Taken: {elapsed_ms:.4f} ms")


def get_source_destination(graph):
    print("\nAvailable locations:", ", ".join(graph.get_nodes()))
    start = input("Enter source location: ").strip()
    goal = input("Enter destination location: ").strip()

    if start not in graph.get_nodes() or goal not in graph.get_nodes():
        print("Invalid location(s) entered. Please check spelling.")
        return None, None
    return start, goal


def main():
    graph = build_city_graph()

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            start, goal = get_source_destination(graph)
            if start:
                (path, nodes_explored), elapsed = measure_time(bfs, graph, start, goal)
                print_path_result("BFS", path, nodes_explored, elapsed)
                if path:
                    draw_graph(graph, path=path, title="BFS Route")

        elif choice == "2":
            start, goal = get_source_destination(graph)
            if start:
                (path, nodes_explored), elapsed = measure_time(dfs, graph, start, goal)
                print_path_result("DFS", path, nodes_explored, elapsed)
                if path:
                    draw_graph(graph, path=path, title="DFS Route")

        elif choice == "3":
            start, goal = get_source_destination(graph)
            if start:
                (path, nodes_explored), elapsed = measure_time(iddfs, graph, start, goal)
                print_path_result("IDDFS", path, nodes_explored, elapsed)
                if path:
                    draw_graph(graph, path=path, title="IDDFS Route")

        elif choice == "4":
            start, goal = get_source_destination(graph)
            if start:
                (path, nodes_explored), elapsed = measure_time(astar, graph, start, goal)
                print_path_result("A* Search", path, nodes_explored, elapsed)
                if path:
                    draw_graph(graph, path=path, title="A* Route")

        elif choice == "5":
            start, goal = get_source_destination(graph)
            if start:
                print("\n========== ALGORITHM COMPARISON ==========")
                algorithms = [("BFS", bfs), ("DFS", dfs), ("IDDFS", iddfs), ("A* Search", astar)]
                print(f"{'Algorithm':<12}{'Path Length':<14}{'Nodes Explored':<16}{'Time (ms)':<12}")
                for name, func in algorithms:
                    (path, nodes_explored), elapsed = measure_time(func, graph, start, goal)
                    path_len = len(path) - 1 if path else "N/A"
                    print(f"{name:<12}{str(path_len):<14}{nodes_explored:<16}{elapsed:<12.4f}")

        elif choice == "6":
            coloring = greedy_coloring(graph)
            num_colors = len(set(coloring.values()))
            print(f"\nMinimum Traffic Signal Groups Needed: {num_colors}")
            for node, color in coloring.items():
                print(f"{node}: Group {color + 1}")
            draw_graph(graph, coloring=coloring, title="Traffic Signal Grouping")

        elif choice == "7":
            draw_graph(graph, title="Smart City Map")

        elif choice == "8":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()