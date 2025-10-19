import tkinter as tk
from algorithms.fibonacci import fib_trace
from ui.stack_view import StackView

class FibonacciVisualizer:
    def __init__(self, root, n=5, delay=700):
        self.root = root
        self.delay = delay
        self.steps = fib_trace(n)
        self.step_index = 0
        self.stack_view = StackView(root)
        self.animate()

    def animate(self):
        if self.step_index < len(self.steps):
            action, value = self.steps[self.step_index]
            if action == "call":
                self.stack_view.push(value)
            else:
                self.stack_view.pop()
            self.step_index += 1
            self.root.after(self.delay, self.animate)
        else:
            tk.Label(self.root, text="✅ Fibonacci Done!", font=("Arial", 16)).pack(pady=10)
