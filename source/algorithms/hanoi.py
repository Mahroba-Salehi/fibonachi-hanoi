def hanoi_moves(n,source=0,target=2,auxiliary=1):

    moves =[]

    def hanoi(n,source,target,auxiliary):
        if n==1:
            moves.append((source,target))
        else:
            hanoi(n-1,source,target,auxiliary)
            moves.append((source,target))
            hanoi(n-1,auxiliary,target,source)

    hanoi(n,source,target,auxiliary)
    return moves