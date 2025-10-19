from algorithms.hanoi import hanoi_moves
from ui.hanoi_view import HanoiView
import tkinter as tk

class HanoiVisualizer:
    def __init__(self, master, n=3, delay=700):
        self.master = master
        self.n = n
        self.delay = delay
        self.rods = [list(range(n, 0, -1)), [], []]
        self.call_stack = []
        self.moves = hanoi_moves(n)
        self.step = 0
        self.view = HanoiView(master, n)
        self.animate()

    def animate(self):
        if self.step < len(self.moves):
            src, tgt = self.moves[self.step]
            self.call_stack.append(f"Move {src}->{tgt}")
            if self.rods[src]:
                disk = self.rods[src].pop()
                self.rods[tgt].append(disk)
            self.view.draw_scene(self.rods, self.call_stack)
            if len(self.call_stack) > 6:
                self.call_stack.pop(0)
            self.step += 1
            self.master.after(self.delay, self.animate)
        else:
            self.view.show_done()
