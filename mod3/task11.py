def check_winner(board, k):
    n = len(board)
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]

    for row in range(n):
        for col in range(n):
            if board[row][col] == '_':
                continue

            for direction in directions:
                dx, dy = direction
                x, y = row, col
                count = 0

                while 0 <= x < n and 0 <= y < n and board[x][y] == board[row][col]:
                    count += 1
                    if count == k:
                        return board[row][col]

                    x += dx
                    y += dy

    return 'Ничья'


k = int(input("Введите порядок квадратного поля: "))
board = []
for i in range(k):
    row = input(f"Введите строку поля длины {k}: ")
    board.append(list(row))

winner = check_winner(board, k)

if winner == 'Ничья':
    print("Ничья")
else:
    print(f"Победитель: {winner}")
