# Smart City Route Planner

A Python-based AI project that models a city as a graph and solves two real-world problems: **finding the best route between two locations** and **assigning traffic signal groups** to intersections. Includes both a command-line interface and a full Tkinter GUI.

## Overview

The city is represented as a weighted graph — locations (Hospital, Mall, School, Airport, etc.) are nodes, and roads connecting them are weighted edges. The project applies classical AI search algorithms to find routes, and a graph coloring algorithm to assign traffic signal groups so that no two connected intersections are active at the same time.

## Features

- **Route Finding** using four search algorithms:
  - BFS (Breadth-First Search)
  - DFS (Depth-First Search)
  - IDDFS (Iterative Deepening DFS)
  - A* Search (with Euclidean distance heuristic)
- **Compare All** — runs all four algorithms on the same route and shows path length, nodes explored, and execution time side by side
- **Traffic Signal Grouping** using Greedy Graph Coloring — assigns the minimum number of signal groups so no two adjacent intersections share a group
- **City Map Visualization** — view the full graph with matplotlib
- **Two interfaces**:
  - CLI: menu-driven text interface
  - GUI: Tkinter interface with dropdowns, algorithm buttons, and an embedded map

## Project Structure

```
smart-city-route-planner/
│
├── main.py                  # CLI entry point
├── gui.py                   # GUI entry point (Tkinter)
├── graph.py                 # Graph data structure
├── data.py                  # Hardcoded city map (nodes, edges, coordinates)
├── utils.py                 # Heuristic function, path reconstruction, timing
├── visualization.py         # Matplotlib visualization (map, path, coloring)
│
├── search_algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── iddfs.py
│   └── astar.py
│
└── coloring/
    └── graph_coloring.py    # Greedy graph coloring
```

## Requirements

- Python 3.x
- matplotlib

Install dependencies:
```bash
pip install matplotlib
```

## How to Run

**CLI version:**
```bash
python main.py
```

**GUI version:**
```bash
python gui.py
```

## Usage

1. Select a source and destination location.
2. Choose an algorithm (BFS / DFS / IDDFS / A*) to find a route, or use **Compare All** to see all four side by side.
3. Use **Traffic Coloring** to see the minimum signal groups needed for the whole city.
4. Use **Show Map** to view the full city graph.

## Sample Output

Example route: Hospital → Airport (via BFS)
```
Path: Hospital -> Mall -> Junction_1 -> Park -> Library -> Airport
Hops: 5
Nodes Explored: 9
Time: 0.0320 ms
```

Example traffic coloring result:
```
Minimum Traffic Signal Groups Needed: 3
Hospital: Group 1
Mall: Group 2
...
```

## Algorithms Used

| Algorithm | Guarantees Shortest Path | Notes |
|-----------|---------------------------|-------|
| BFS       | Yes                       | Explores level by level |
| DFS       | No                        | Fast but not optimal |
| IDDFS     | Yes                       | Optimal but explores more nodes (repeated re-exploration) |
| A*        | Yes                       | Optimal and explores fewer nodes using a heuristic |

## Notes

- The city graph is currently hardcoded with 15 locations.
- Greedy Graph Coloring is order-dependent and may not always produce the mathematically minimum number of colors.
