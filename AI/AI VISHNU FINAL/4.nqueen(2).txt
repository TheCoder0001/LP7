def is_safe(b, r, c):
    for i in range(r):
        if b[i] == c or abs(b[i]-c) == r-i:
            return False
    return True

def solve(b, r, n):
    if r == n:
        return b
    for c in range(n):
        if is_safe(b, r, c):
            b[r] = c
            res = solve(b, r+1, n)
            if res: return res
    return None

def print_board(b, n):
    for i in range(n):
        print(' '.join(' Q ' if j == b[i] else '.' for j in range(n)))

n = 4
board = [-1]*n
sol = solve(board, 0, n)
if sol:
    print_board(sol, n)
