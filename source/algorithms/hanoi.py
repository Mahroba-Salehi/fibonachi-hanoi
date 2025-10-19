def hanoi_moves(n, source=0, target=2, auxiliary=1):
    moves = []

    def hanoi(n, src, tgt, aux):
        if n == 1:
            moves.append((src, tgt))
        else:
            hanoi(n-1, src, aux, tgt)
            moves.append((src, tgt))
            hanoi(n-1, aux, tgt, src)

    hanoi(n, source, target, auxiliary)
    return moves
