import tkinter as tk
from visualizer import StackVisualizer
from algorithms import fib, hanoi

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Call Stack Visualizer")
    vis = StackVisualizer(root, delay=0.5)

    # demo: Fibonacci
    print("Fibonacci(5) = ", fib(5, vis))


    root.mainloop()
