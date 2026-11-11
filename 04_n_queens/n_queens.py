def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def solve(board, row, n):
    if row == n:
        return True
    if 1 in board[row]:
        return solve(board, row + 1, n)
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


n = int(input("Enter n: "))
col = int(input(f"Column for first queen in row 0 (0 to {n - 1}): "))

board = [[0] * n for _ in range(n)]
board[0][col] = 1

if solve(board, 0, n):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
else:
    print("No solution with this first queen position")
