import tkinter as tk
import time


class StackVisualizer:

    def __init__(self, root, width=400, height=500, delay=0.5):

        self.root = root
        self.width = width
        self.height = height
        self.delay = delay
        self.stack = []

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.canvas.create_text(
            self.width // 2, 20,
            text="Stack Visualization",
            font=("Arial", 14, "bold"),
            fill="black"
        )

    def draw_stack(self):
     self.canvas.delete("frame")

        box_height = 40
        padding = 10
        base_y = self.height - 30

        for i, frame_name in enumerate(reversed(self.stack)):
            y_bottom = base_y - i * (box_height + padding)
            y_top = y_bottom - box_height
            x_left = 80
            x_right = self.width - 80

            self.canvas.create_rectangle(
                x_left, y_top, x_right, y_bottom,
                fill="lightblue", outline="black", tags="frame"
            )

            self.canvas.create_text(
                (x_left + x_right) // 2, (y_top + y_bottom) // 2,
                text=frame_name, font=("Arial", 11, "bold"), tags="frame"
            )

        self.root.update()
        time.sleep(self.delay)

    def push(self, frame_name):
        self.stack.append(frame_name)
        self.draw_stack()

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.draw_stack()
