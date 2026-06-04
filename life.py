import tkinter as tk
import random

ROWS = 45
COLS = 50
CELL_SIZE = 10
SPEED = 50   # smaller = faster/smoother, example: 50 ms

board = []

for i in range(ROWS): # creating random cells (active/disactive)
    row = []
    for j in range(COLS):
        row.append(random.choice([0, 0, 0, 1]))
    board.append(row)


def count_neighbors(x, y):# counts the neighbours for the affectation 
    count = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):

            if i == x and j == y:
                continue

            if 0 <= i < ROWS and 0 <= j < COLS:
                count += board[i][j]

    return count


def next_generation(): # generates the new grid containing the next state of the cells (next iteration)
    global board

    new_board = []

    for i in range(ROWS):
        new_row = []

        for j in range(COLS):
            neighbors = count_neighbors(i, j)

            if board[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                new_row.append(1)
            elif board[i][j] == 0 and neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)

        new_board.append(new_row)

    board = new_board


def update_colors(): # used to fill the cells with color 
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 1:
                canvas.itemconfig(rectangles[i][j], fill="black")
            else:
                canvas.itemconfig(rectangles[i][j], fill="white")


def update():
    update_colors()
    next_generation()
    window.after(SPEED, update)


window = tk.Tk() # tkiner library to open window 
window.title("Game of Life")

canvas = tk.Canvas(
    window,
    width=COLS * CELL_SIZE,
    height=ROWS * CELL_SIZE,
    bg="white"
)

canvas.pack()

rectangles = []

for i in range(ROWS):
    row = []

    for j in range(COLS):
        x1 = j * CELL_SIZE
        y1 = i * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE

        rect = canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill="white",
            outline=""
        )

        row.append(rect)

    rectangles.append(row)

update()

window.mainloop()