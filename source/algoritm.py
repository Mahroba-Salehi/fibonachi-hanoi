from time import sleep

def fib(n, visualizer):
    visualizer.push(f"fib({n})")
    if n <= 1:
        result = n
    else:
        a = fib(n - 1, visualizer)
        b = fib(n - 2, visualizer)
        result = a + b
    visualizer.pop()
    return result

def hanoi(n, source, target, auxiliary, visualizer):
    visualizer.push(f"hanoi({n}, {source}->{target})")
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n-1, source, auxiliary, target, visualizer)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n-1, auxiliary, target, source, visualizer)
    visualizer.pop()
