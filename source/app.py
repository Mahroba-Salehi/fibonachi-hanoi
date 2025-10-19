import tkinter as tk
from fibonacci_visual import FibonacciVisualizer
from hanoi_visual import HanoiVisualizer

def run_fibonacci():
    for widget in main_frame.winfo_children():
        widget.destroy()
    FibonacciVisualizer(main_frame, n=5, delay=700)

def run_hanoi():
    for widget in main_frame.winfo_children():
        widget.destroy()
    HanoiVisualizer(main_frame, n=3, delay=800)

root = tk.Tk()
root.title("Algorithm Visualizer")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Visualize Fibonacci", command=run_fibonacci, width=20).pack(side="left", padx=10)
tk.Button(button_frame, text="Visualize Tower of Hanoi", command=run_hanoi, width=20).pack(side="left", padx=10)

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

root.mainloop()
