import tkinter as tk

class HanoiView:
    def __init__(self, master, n):
        self.canvas = tk.Canvas(master, width=600, height=480, bg="#fafafa")
        self.canvas.pack()
        self.n = n
        self.colors = ["#D487BA", "#656EC8", "#BB8744", "#9ED487", "#87D4D2"]

    def draw_scene(self, rods, call_stack):
        self.canvas.delete("all")
        for i in range(3):
            x_center = 120 + i * 200
            self.canvas.create_rectangle(x_center - 5, 100, x_center + 5, 300, fill="#888")
            for j, disk in enumerate(rods[i]):
                y = 280 - j * 25
                width = disk * 25
                color = self.colors[(disk - 1) % len(self.colors)]
                self.canvas.create_rectangle(x_center - width, y - 20, x_center + width, y, fill=color, outline="#555")
        self.canvas.create_text(300, 320, text="Call Stack:", font=("Consolas", 12, "bold"), fill="#333")
        y = 340
        for i, frame in enumerate(reversed(call_stack[-6:])):
            self.canvas.create_text(300, y + i * 20, text=frame, font=("Consolas", 10), fill="#444")
        self.canvas.update()

    def show_done(self):
        self.canvas.create_text(300, 440, text="Hanoi done!", font=("Arial", 14, "bold"), fill="#222")
