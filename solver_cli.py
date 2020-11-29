"""Command line solver.
Uses recursion to solve any solveable Sudoku puzzle."""

def is_possible(game, r, c, v):
    """is_possible(row, column, value)
    determine is value is possible in the game position"""
    # Check the columns of the row
    for i in game[r]:
        if i == v:
            return False

    # Check lines of the column
    for lin in range(9):
        if game[lin][c] == v:
            return False

    # Check the quarter area
    r0 = (r // 3) * 3  # 0, 3 or 6
    c0 = (c // 3) * 3 
    for lin in range(3):
        for col in range(3):
            if game[lin + r0][col + c0] == v:
                return False

    return True

def solve(game):
    for r in range(9):
        for c in range(9):
            # zero position (empty)
            if game[r][c] == 0:                                
                for i in range(1, 10):
                    if is_possible(game, r, c, i):
                        game[r][c] = i
                        solve(game)
                        game[r][c] = 0
                return

    # prints out the solved puzzle
    print(*game, sep="\n")
    exit()


if __name__ == "__main__":
    game = [[0 for x in range(9)] for _ in range(9)]
    for lin in range(9):
        values = [int(i) for i in input(f"Lin {lin+1}: ")]
        game[lin][:len(values)] = values
    print("# Original game:")        
    print(*game, sep="\n")

    print("\n# Solved game:")
    solve(game)
