def checkmate(board_str):
    try:
        grid = board_str.strip().split('\n')
        size = len(grid)
        board = [list(row) for row in grid]

        # Ensure board is square
        if any(len(row) != size for row in board):
            print("Error")
            return

        # Find King
        king_found = False
        for r in range(size):
            for c in range(size):
                if board[r][c] == 'K':
                    king_row, king_col = r, c
                    king_found = True
                    break
            if king_found:
                break

        if not king_found:
            print("Error")
            return

        # Define piece movement patterns
        threats = {
            'Q': [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)],
            'R': [(-1,0),(1,0),(0,-1),(0,1)],
            'B': [(-1,-1),(-1,1),(1,-1),(1,1)],
            'P': [(1,-1), (1,1)],
        }

        for piece, moves in threats.items():
            for dr, dc in moves:
                x, y = king_row + dr, king_col + dc

                while 0 <= x < size and 0 <= y < size:
                    cell = board[x][y]
                    if cell == '.':
                        x += dr
                        y += dc
                        continue
                    elif cell == piece or (piece == 'Q' and cell == 'Q'):
                        print("Success")
                        return
                    else:
                        break

        print("Fail")

    except:
        print("Error")
