import tkinter as tk
from algorithms.hanoi import hanoi_moves
from ui.hanoi_view import HanoiView

class HanoiVisualizer:
    def __init__(self, root, n=3, delay=800):
        self.root = root
        self.delay = delay
        self.n = n
        self.moves = hanoi_moves(n)
        self.step_index = 0
        self.hanoi_view = HanoiView(root, n)
        self.animate()

    def animate(self):
        if self.step_index < len(self.moves):
            src, tgt = self.moves[self.step_index]
            self.hanoi_view.move_disk(src, tgt)
            self.step_index += 1
            self.root.after(self.delay, self.animate)
        else:
            tk.Label(self.root, text="🎉 Tower of Hanoi Done!", font=("Arial", 16)).pack(pady=10)
