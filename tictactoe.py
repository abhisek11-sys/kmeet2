import random

print("WELCOME TO TIC-TAC-TOE!")
print("Player: X")
print("Computer: O")

def print_grid(grid):
    print("Current Grid:")
    print("-------------")
    print("| {} | {} | {} |".format(grid[0][0], grid[0][1], grid[0][2]))
    print("-------------")
    print("| {} | {} | {} |".format(grid[1][0], grid[1][1], grid[1][2]))
    print("-------------")
    print("| {} | {} | {} |".format(grid[2][0], grid[2][1], grid[2][2]))
    print("-------------")

grid = [[' ' for _ in range(3)] for _ in range(3)]
win = 0
while win == 0:
    print_grid(grid)
    player_move = input("Enter your move (row and column) as 'row,col': ")
    computer_move = (random.randint(0, 2), random.randint(0, 2))
    if player_move:
        row, col = map(int, player_move.split(','))
        if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == ' ':
            grid[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
    if computer_move:
        row, col = computer_move
        if grid[row][col] == ' ':
            grid[row][col] = 'O'
    if (grid[0][0] == grid[0][1] == grid[0][2] != ' ') or \
       (grid[1][0] == grid[1][1] == grid[1][2] != ' ') or \
       (grid[2][0] == grid[2][1] == grid[2][2] != ' ') or \
       (grid[0][0] == grid[1][0] == grid[2][0] != ' ') or \
       (grid[0][1] == grid[1][1] == grid[2][1] != ' ') or \
       (grid[0][2] == grid[1][2] == grid[2][2] != ' ') or \
       (grid[0][0] == grid[1][1] == grid[2][2] != ' ') or \
       (grid[0][2] == grid[1][1] == grid[2][0] != ' '):
        win = 1
        print_grid(grid)
        print("Game Over!")
        if grid[row][col] == 'X':
            print("Player wins!")
        else:
            print("Computer wins!") 



