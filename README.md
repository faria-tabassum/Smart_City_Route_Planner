# Smart City Route Planner

An AI lab project that models a city as a graph and demonstrates classic
search and graph algorithms — **BFS**, **DFS**, **IDDFS**, **A\* Search**,
and **Graph Coloring** — through a simple, menu-driven console application
with graph visualization.

The city is represented as a weighted graph where locations (hospital,
mall, school, junctions, etc.) are nodes and roads connecting them are
edges. The project lets you find routes between any two locations using
different search strategies, compare their performance, and solve a
traffic-signal scheduling problem using graph coloring.

## Features

-  **Predefined city map** — 15 locations connected by weighted roads
-  **Route finding** with 4 different search algorithms (BFS, DFS,
  IDDFS, A*)
-  **Algorithm comparison mode** — runs all 4 algorithms on the same
  source/destination and compares path length, nodes explored, and
  execution time
-  **Traffic signal coloring** — assigns the minimum number of signal
  groups so that no two connected intersections share the same group
-  **Graph visualization** — renders the city map, the found path, and
  the signal grouping using `matplotlib` and `networkx`
-  **Menu-driven CLI** — no GUI dependencies beyond visualization

## Algorithms & Why They're Used

| Algorithm | Role in the project | Concept demonstrated |
|---|---|---|
| **BFS** | Finds the route with the fewest road segments (hops) | Uninformed search, shortest path in an unweighted sense |
| **DFS** | Explores reachable locations via backtracking | Recursion, connectivity |
| **IDDFS** | Combines BFS's optimality with DFS's low memory usage | Iterative deepening, depth-limited search |
| **A\*** | Finds the shortest-cost route using real distances + a heuristic | Informed search, heuristic design, priority queues |
| **Graph Coloring** | Groups intersections into non-conflicting traffic signal phases | Greedy coloring, constraint satisfaction |

## Project Structure

```
smart_city_route_planner/
├── main.py                     
├── graph.py                    
├── data.py                     
├── utils.py                    
├── visualization.py          
├── search_algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── iddfs.py
│   └── astar.py
└── coloring/
    └── graph_coloring.py      
```

You'll see a menu:

```
===== SMART CITY ROUTE PLANNER =====
1. Find Route using BFS
2. Find Route using DFS
3. Find Route using IDDFS
4. Find Route using A* Search
5. Compare All Algorithms
6. Traffic Signal Coloring
7. Show City Map
8. Exit
```

- Options **1–4**: enter a source and destination location (e.g.
  `Hospital` → `Airport`) to find a route with that algorithm.
- Option **5**: enter a source and destination to see a side-by-side
  comparison of all four algorithms (path length, nodes explored, time
  taken).
- Option **6**: computes and displays the minimum number of traffic
  signal groups needed, then visualizes the grouping.
- Option **7**: displays the full city map.

Available location names are printed before each query — enter them
exactly as shown (e.g. `Junction_1`, `Junction_2`).

## Sample Output

```
[BFS]
Path: Hospital -> Mall -> Junction_1 -> Bank -> Junction_2 -> Airport
Total Stops: 5
Nodes Explored: 9
Time Taken: 0.0437 ms
```

## Future Improvements

- Load city data from a JSON/CSV file instead of hardcoding it
- Add a GUI (e.g. `tkinter`) as an alternative to the CLI
- Support user-defined custom city maps
