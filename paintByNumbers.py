from tkinter import *

#TODO: Put each class in its own file

class Cell():
    global FILLED_COLOR_BG
    global FILLED_COLOR_BORDER

    FILLED_COLOR_BG = "black"
    FILLED_COLOR_BORDER = "black"
    EMPTY_COLOR_BG = "white"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill= not self.fill

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        if self.master != None :
            fill = FILLED_COLOR_BG
            outline = FILLED_COLOR_BORDER

            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)


class ChangeColor():
    def black(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "black"
        FILLED_COLOR_BORDER = "black"

    def blue(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "blue"
        FILLED_COLOR_BORDER = "blue"
        
    def red(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "red"
        FILLED_COLOR_BORDER = "red"
    
    def orange(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "orange"
        FILLED_COLOR_BORDER = "orange"
        
    def yellow(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "yellow"
        FILLED_COLOR_BORDER = "yellow"
        
    def green(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "green"
        FILLED_COLOR_BORDER = "green"

    def purple(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "purple"
        FILLED_COLOR_BORDER = "purple"

    def white(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "white"
        FILLED_COLOR_BORDER = "white"

    
    
class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):
            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))
            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of modified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        #add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)


if __name__ == "__main__" :
    app = Tk()

    black = Button(app, text = "black")
    black.bind("<Button-1>", ChangeColor.black)
    black.pack()
    
    blue = Button(app, text = "blue")
    blue.bind("<Button-1>", ChangeColor.blue)
    blue.pack()
    
    red = Button(app, text = "red")
    red.bind("<Button-1>", ChangeColor.red)
    red.pack()

    orange = Button(app, text = "orange")
    orange.bind("<Button-1>", ChangeColor.orange)
    orange.pack()
    
    yellow = Button(app, text = "yellow")
    yellow.bind("<Button-1>", ChangeColor.yellow)
    yellow.pack()

    #blue = Button(app, text = "blue")
    #blue.bind("<Button-1>", ChangeColor.blue)
    #blue.pack()

    #blue = Button(app, text = "blue")
    #blue.bind("<Button-1>", ChangeColor.blue)
    #blue.pack()

    #blue = Button(app, text = "blue")
    #blue.bind("<Button-1>", ChangeColor.blue)
    #blue.pack()


    cellGrid = CellGrid(app, 50, 50, 15)
    cellGrid.pack()
    
    app.mainloop()

    #makes two drop down menus, but nothing happens when clicked
    #menubar = Menu(app)
    #menubar = Menu(menubar, tearoff=0)
    #menubar.add_command(label="Black", command = lambda: ChangeColor.black)
    #menubar.add_command(label="Blue", command = lambda: ChangeColor.blue)
    #app.config(menu=menubar)

    #makes buttons for each color, but no color change occurs when clicked
    #black = Button(app, text = "black", command = lambda: ChangeColor.black)
    #black.pack()
    #blue = Button(app, text = "blue", command = lambda: ChangeColor.blue)
    #blue.pack()