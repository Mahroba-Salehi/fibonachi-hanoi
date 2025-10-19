import tkinter as tk

class HanoiView:
    def __init__(self, master, num_disks):
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
        self.num_disks = num_disks
        self.rods = [list(range(num_disks, 0, -1)), [], []]
        self.colors = ["#D487BA", "#656EC8", "#BB8744", "#9ED487", "#87D4D2"]
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for i in range(3):
            x = 120 + i*200
            self.canvas.create_rectangle(x-5, 80, x+5, 280, fill="gray")
            rod = self.rods[i]
            for j, disk in enumerate(rod):
                y = 260 - j*25
                width = disk*20
                self.canvas.create_rectangle(x-width, y-20, x+width, y, fill=self.colors[disk-1])
        self.canvas.update()

    def move_disk(self, src, tgt):
        disk = self.rods[src].pop()
        self.rods[tgt].append(disk)
        self.draw()
