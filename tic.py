import pygame
import sys
import tkinter
from tkinter import messagebox

# Define constants for the game
BOARD_SIZE = 3
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 350
LINE_WIDTH = 10
CELL_SIZE = 120
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
# Set the background to white
screen.fill((255, 255, 255))
pygame.display.flip()

# initialise tkinter for the messagebox
root = tkinter.Tk()
root.withdraw()

# Define helper functions for drawing the board
def draw_board():
    # Draw the horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (0, CELL_SIZE), (WINDOW_WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, (0, 0, 0), (0, CELL_SIZE * 2), (WINDOW_WIDTH, CELL_SIZE * 2), LINE_WIDTH)
    # Draw the vertical lines
    pygame.draw.line(screen, (0, 0, 0), (CELL_SIZE, 0), (CELL_SIZE, WINDOW_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, (0, 0, 0), (CELL_SIZE * 2, 0), (CELL_SIZE * 2, WINDOW_HEIGHT), LINE_WIDTH)
    # apply the lines
    pygame.display.update()

def clear_board():
    global screen
    screen.fill((255, 255, 255))

def draw_x(row, col):
    # Draw an X at the given row and column
    x_pos = col * CELL_SIZE + CELL_SIZE // 2
    y_pos = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.line(screen, X_COLOR, (x_pos - CELL_SIZE // 4, y_pos - CELL_SIZE // 4),
                     (x_pos + CELL_SIZE // 4, y_pos + CELL_SIZE // 4), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (x_pos - CELL_SIZE // 4, y_pos + CELL_SIZE // 4),
                     (x_pos + CELL_SIZE // 4, y_pos - CELL_SIZE // 4), LINE_WIDTH)

def draw_o(row, col):
    # Draw an O at the given row and column
    x_pos = col * CELL_SIZE + CELL_SIZE // 2
    y_pos = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, O_COLOR, (x_pos, y_pos), CELL_SIZE // 4, LINE_WIDTH)

def get_row_col_from_mouse_pos(pos):
    # Given a mouse position, return the corresponding row and column on the board
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

def end_game(winner=''):
    # messagebox.showinfo("Game Over", f"Player {winner} wins!")
    # messagebox.showinfo("Draw", f"The game has been tied!")
    if winner:
        answer = messagebox.askquestion("Game Over", f"Player {winner} wins!" + " Do you wish to restart the game?")
    else:
        answer = messagebox.askquestion("Draw", f"The game has been tied!" + " Do you wish to restart the game?")

    if answer == 'yes':
        clear_board()
        draw_board()
        play_game()
    else:
        sys.exit()
    return

# Define the main game loop
def play_game():
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player = 'X'
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the row and column of the cell that was clicked
                row, col = get_row_col_from_mouse_pos(pygame.mouse.get_pos())
                if board[row][col] == ' ':
                    board[row][col] = player
                    if player == 'X':
                        draw_x(row, col)
                        player = 'O'
                    else:
                        draw_o(row, col)
                        player = 'X'
                    pygame.display.update()

                    # Check if there is a winner
                    for i in range(BOARD_SIZE):
                        # vertical
                        if board[i][0] == board[i][1] == board[i][2] != ' ':
                            end_game(board[i][0])
                        # horizontal
                        if board[0][i] == board[1][i] == board[2][i] != ' ':
                            end_game(board[0][i])
                    # diagonal (top left - bottom right)
                    if board[0][0] == board[1][1] == board[2][2] != ' ':
                        end_game(board[0][0])
                    # diagonal (bottom left - top right)
                    if board[0][2] == board[1][1] == board[2][0] != ' ':
                        end_game(board[0][2])

                    # check for draw
                    if all(all(item != ' ' for item in items) for items in board):
                        end_game()


if __name__ == "__main__":
    draw_board()
    play_game()