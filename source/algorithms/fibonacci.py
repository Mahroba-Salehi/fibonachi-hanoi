def fib_trace(n):

    steps=[]

    def fib(k):
        steps.append(("call", k))
        if k <= 1:
            steps.append(("return", k))
            return k
        val = fib(n - 1) + fib(n - 2)
        steps.append(("return", k))
        return val

    fib(n)
    return steps


