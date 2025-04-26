# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as 
# rectangles on the screen. We then create an eraser rectangle which,
#  when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

CANVAS_HEIGHT : int = 400
CANVAS_WIDTH : int = 400
CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def create_grid(canvas):
    cell =[]
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect= canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='black')
            row_cells.append(rect)
            cell.append(row_cells)
    return cell
def main():
    root = tk.Tk()
    root.title("Grid exmple")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
    canvas.pack()

    # Create the grid of blue cells
    grid = create_grid(canvas)

    # Create the eraser rectangle
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='white', outline='black')

    def move_eraser(event):
        x = event.x - ERASER_SIZE // 2
        y = event.y - ERASER_SIZE // 2
        canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        erase_cells(x, y)

    def erase_cells(x, y):
        for row in grid:
            for rect in row:
                rect_coords = canvas.coords(rect)
                if (rect_coords[0] < x + ERASER_SIZE and rect_coords[2] > x and
                        rect_coords[1] < y + ERASER_SIZE and rect_coords[3] > y):
                    canvas.itemconfig(rect, fill='white')

    canvas.bind("<B1-Motion>", move_eraser)
    root.mainloop()
if __name__ == "__main__":
    main()