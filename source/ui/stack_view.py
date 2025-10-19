import tkinter as tk

class StackView:
    def __init__(self, master, x=50, y=300, width=200):
        self.canvas = tk.Canvas(master, width=width+100, height=400, bg="white")
        self.canvas.pack()
        self.stack = []
        self.x = x
        self.y = y
        self.width = width

    def draw(self):
        self.canvas.delete("all")
        y = self.y
        for item in reversed(self.stack):
            self.canvas.create_rectangle(self.x, y-40, self.x+self.width, y, fill="#add8e6", outline="black")
            self.canvas.create_text(self.x + self.width/2, y-20, text=f"fib({item})")
            y -= 45
        self.canvas.update()

    def push(self, value):
        self.stack.append(value)
        self.draw()

    def pop(self):
        if self.stack:
            self.stack.pop()
        self.draw()
