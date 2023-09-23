import tkinter as tk
from queue import PriorityQueue

# Taille de la grille et la vitesse d'exécution de l'algorithme
GRID_SIZE = 16
SLEEP_TIME = 5

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_start = False
        self.is_end = False
        self.is_wall = False
        self.neighbors = []
        self.parent = None
        self.g = float('inf')
        self.h = float('inf')

    def __lt__(self, other):
        # Utilisé pour la priorité dans la file de priorité
        return (self.g + self.h) < (other.g + other.h)

class AStarVisualizer:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.grid = [[Node(row, col) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
        self.start_node = None
        self.end_node = None
        self.is_dragging = False
        self.is_running = False

    def create_grid(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                node = self.grid[row][col]
                x1, y1 = col * 20, row * 20
                x2, y2 = x1 + 20, y1 + 20
                color = "white" if not node.is_wall else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.canvas.create_text(x1 + 10, y1 + 10, text=str(node.g + node.h), fill="red")

    def clear_grid(self):
        for row in self.grid:
            for node in row:
                node.is_start = False
                node.is_end = False
                node.is_wall = False
                node.neighbors = []
                node.parent = None
                node.g = float('inf')
                node.h = float('inf')
        self.start_node = None
        self.end_node = None

    def on_click(self, event):
        if not self.is_running:
            col = event.x // 20
            row = event.y // 20
            node = self.grid[row][col]

            if not self.start_node:
                node.is_start = True
                self.start_node = node
            elif not self.end_node:
                node.is_end = True
                self.end_node = node
            else:
                node.is_wall = not node.is_wall
            self.draw_node(node)

    def on_drag(self, event):
        if not self.is_running:
            col = event.x // 20
            row = event.y // 20
            node = self.grid[row][col]
            if not node.is_start and not node.is_end:
                node.is_wall = True
                self.draw_node(node)

    def on_release(self, event):
        self.is_dragging = False

    def draw_node(self, node):
        x1, y1 = node.col * 20, node.row * 20
        x2, y2 = x1 + 20, y1 + 20
        color = "white" if not node.is_wall else "black"
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_path(self, end_node):
        current = end_node
        while current:
            x1, y1 = current.col * 20 + 10, current.row * 20 + 10
            if current.is_end:
                self.canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="green")
            elif current.is_start:
                self.canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="blue")
            else:
                self.canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="yellow")
            current = current.parent

    def heuristic(self, node):
        return abs(node.row - self.end_node.row) + abs(node.col - self.end_node.col)

    def find_neighbors(self, node):
        neighbors = []
        row, col = node.row, node.col
        if row > 0:
            neighbors.append(self.grid[row - 1][col])
        if row < GRID_SIZE - 1:
            neighbors.append(self.grid[row + 1][col])
        if col > 0:
            neighbors.append(self.grid[row][col - 1])
        if col < GRID_SIZE - 1:
            neighbors.append(self.grid[row][col + 1])
        return neighbors

    def run_astar(self):
        if not self.start_node or not self.end_node:
            return

        open_set = PriorityQueue()
        open_set.put(self.start_node)
        self.start_node.g = 0
        self.start_node.h = self.heuristic(self.start_node)

        while not open_set.empty():
            current_node = open_set.get()

            if current_node == self.end_node:
                self.is_running = False
                self.draw_path(self.end_node)
                break

            if current_node != self.start_node:
                self.canvas.create_rectangle(current_node.col * 20, current_node.row * 20, (current_node.col + 1) * 20, (current_node.row + 1) * 20, fill="blue")

            for neighbor in self.find_neighbors(current_node):
                if neighbor.is_wall:
                    continue

                tentative_g = current_node.g + 1

                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor)

                    if neighbor not in open_set.queue:
                        open_set.put(neighbor)

            self.root.update()
            self.root.after(SLEEP_TIME)

    def start_algorithm(self):
        if not self.is_running:
            self.is_running = True
            self.run_astar()

    def clear_board(self):
        if not self.is_running:
            self.canvas.delete("all")
            self.clear_grid()
            self.create_grid()

    def run(self):
        self.create_grid()
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        start_button = tk.Button(self.root, text="Start", command=self.start_algorithm)
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_board)

        start_button.pack()
        clear_button.pack()

        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("A* Pathfinding Visualization")

    canvas = tk.Canvas(root, width=GRID_SIZE * 20, height=GRID_SIZE * 20)
    canvas.pack()

    visualizer = AStarVisualizer(root, canvas)
    visualizer.run()
