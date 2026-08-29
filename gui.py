import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from data import build_city_graph
from search_algorithms.bfs import bfs
from search_algorithms.dfs import dfs
from search_algorithms.iddfs import iddfs
from search_algorithms.astar import astar
from coloring.graph_coloring import greedy_coloring
from utils import measure_time
from visualization import build_figure


class SmartCityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart City Route Planner")
        self.root.geometry("1150x700")

        self.graph = build_city_graph()
        self.canvas = None  

        self._build_layout()
        self._show_map()  

   
    def _build_layout(self):
       
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(control_frame, text="Source:").grid(row=0, column=0, padx=5)
        self.source_var = tk.StringVar()
        source_dropdown = ttk.Combobox(
            control_frame, textvariable=self.source_var,
            values=self.graph.get_nodes(), state="readonly", width=15
        )
        source_dropdown.grid(row=0, column=1, padx=5)

        tk.Label(control_frame, text="Destination:").grid(row=0, column=2, padx=5)
        self.dest_var = tk.StringVar()
        dest_dropdown = ttk.Combobox(
            control_frame, textvariable=self.dest_var,
            values=self.graph.get_nodes(), state="readonly", width=15
        )
        dest_dropdown.grid(row=0, column=3, padx=5)

        
        button_frame = tk.Frame(self.root, padx=10, pady=5)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        buttons = [
            ("BFS", lambda: self.run_algorithm("BFS", bfs), "#4C6EF5", "#3B5BDB"),
            ("DFS", lambda: self.run_algorithm("DFS", dfs), "#12B886", "#0CA678"),
            ("IDDFS", lambda: self.run_algorithm("IDDFS", iddfs), "#F59F00", "#E8590C"),
            ("A* Search", lambda: self.run_algorithm("A* Search", astar), "#E64980", "#D6336C"),
            ("Compare All", self.compare_all, "#7048E8", "#5F3DC4"),
            ("Traffic Coloring", self.run_coloring, "#E03131", "#C92A2A"),
            ("Show Map", self._show_map, "#495057", "#343A40"),
        ]
        for text, command, color, hover_color in buttons:
            self._make_color_button(button_frame, text, command, color, hover_color)

        
        main_frame = tk.Frame(self.root)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.plot_frame = tk.Frame(main_frame, width=750, height=600)
        self.plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        output_frame = tk.Frame(main_frame, width=350)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        tk.Label(output_frame, text="Output", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)
        self.output_text = tk.Text(output_frame, width=45, height=35, wrap="word")
        self.output_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def _make_color_button(self, parent, text, command, color, hover_color):
        """A raw Canvas rectangle + text acting as a button. This draws the
        color directly as graphics instead of setting a widget's background
        property, so no OS theme, high-contrast mode, or Tk color scheme can
        override it — this is the most bulletproof way to guarantee color."""
        width, height = 130, 42
        canvas = tk.Canvas(
            parent, width=width, height=height,
            highlightthickness=0, bd=0, cursor="hand2",
        )
        canvas.pack(side=tk.LEFT, padx=4)

        rect = canvas.create_rectangle(0, 0, width, height, fill=color, outline=color)
        label = canvas.create_text(
            width / 2, height / 2, text=text, fill="white",
            font=("Arial", 10, "bold"),
        )

        def on_click(event):
            command()

        def on_enter(event):
            canvas.itemconfig(rect, fill=hover_color, outline=hover_color)

        def on_leave(event):
            canvas.itemconfig(rect, fill=color, outline=color)

        canvas.tag_bind(rect, "<Button-1>", on_click)
        canvas.tag_bind(label, "<Button-1>", on_click)
        canvas.bind("<Button-1>", on_click)
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        return canvas

    def _get_source_destination(self):
        start = self.source_var.get()
        goal = self.dest_var.get()
        if not start or not goal:
            messagebox.showwarning("Missing input", "Please select both source and destination.")
            return None, None
        return start, goal

    def _render_figure(self, fig):
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
            plt.close("all")

        self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _log(self, text):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

    def run_algorithm(self, name, func):
        start, goal = self._get_source_destination()
        if not start:
            return

        (path, nodes_explored), elapsed = measure_time(func, self.graph, start, goal)

        if path is None:
            self._log(f"[{name}]\nNo path found between {start} and {goal}.")
            return

        result = (
            f"[{name}]\n\n"
            f"Path:\n{' -> '.join(path)}\n\n"
            f"Total Stops: {len(path) - 1}\n"
            f"Nodes Explored: {nodes_explored}\n"
            f"Time Taken: {elapsed:.4f} ms"
        )
        self._log(result)

        fig = build_figure(self.graph, path=path, title=f"{name} Route: {start} -> {goal}")
        self._render_figure(fig)

    def compare_all(self):
        start, goal = self._get_source_destination()
        if not start:
            return

        algorithms = [("BFS", bfs), ("DFS", dfs), ("IDDFS", iddfs), ("A* Search", astar)]
        lines = [f"Comparison: {start} -> {goal}\n"]
        lines.append(f"{'Algo':<10}{'Stops':<8}{'Explored':<10}{'Time(ms)':<10}")

        best_path = None
        for name, func in algorithms:
            (path, nodes_explored), elapsed = measure_time(func, self.graph, start, goal)
            path_len = len(path) - 1 if path else "N/A"
            lines.append(f"{name:<10}{str(path_len):<8}{nodes_explored:<10}{elapsed:<10.4f}")
            if name == "BFS" and path:
                best_path = path

        self._log("\n".join(lines))

        if best_path:
            fig = build_figure(self.graph, path=best_path, title=f"BFS Route: {start} -> {goal}")
            self._render_figure(fig)

    def run_coloring(self):
        coloring = greedy_coloring(self.graph)
        num_colors = len(set(coloring.values()))

        lines = [f"Minimum Traffic Signal Groups Needed: {num_colors}\n"]
        for node, color in coloring.items():
            lines.append(f"{node}: Group {color + 1}")
        self._log("\n".join(lines))

        fig = build_figure(self.graph, coloring=coloring, title="Traffic Signal Grouping")
        self._render_figure(fig)

    def _show_map(self):
        self._log("Showing the full city map.\nSelect a source and destination, then pick an algorithm.")
        fig = build_figure(self.graph, title="Smart City Map")
        self._render_figure(fig)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCityApp(root)
    root.mainloop()
