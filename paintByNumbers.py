from tkinter import *
import Colors

class Cell():
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
                fill = EMPTY_COLOR_BG
                outline = EMPTY_COLOR_BORDER
        xmin = self.abs * self.size
        xmax = xmin + self.size
        ymin = self.ord * self.size
        ymax = ymin + self.size

        self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)


class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        #creation of grid. rowNumber and columnNumber are inputs from main() statement
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

#Clear ability to empty a cell of any color data
class Clear():
    def change(self):
        global cellGrid
        cellGrid.destroy()
        cellGrid = CellGrid(app, 50, 50, 15)
        cellGrid.pack()

    def button():
        clear = Button(buttonFrame, text = "Full Clear", width = 10)
        clear.bind("<Button-1>", Clear.change)
        clear.pack(side = LEFT)    

#Each color has a class so that they can be more easily adjusted
class White():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "white"
        FILLED_COLOR_BORDER = "white"

    def button():
        white = Button(buttonFrame, text = "White", width = 7)
        white.bind("<Button-1>", White.change)
        white.pack(side = LEFT)

class Black():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "black"
        FILLED_COLOR_BORDER = "black"

    def button():
        black = Button(buttonFrame, text = "Black", width = 7)
        black.bind("<Button-1>", Black.change)
        black.pack(side = LEFT)

class Purple():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "purple"
        FILLED_COLOR_BORDER = "purple"

    def button():
        purple = Button(buttonFrame, text = "Purple", width = 7)
        purple.bind("<Button-1>", Purple.change)
        purple.pack(side = LEFT)

class Orange():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "orange"
        FILLED_COLOR_BORDER = "orange"

    def button():
        orange = Button(buttonFrame, text = "Orange", width = 7)
        orange.bind("<Button-1>", Orange.change)
        orange.pack(side = LEFT)

class Green():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "green"
        FILLED_COLOR_BORDER = "green"

    def button():
        green = Button(buttonFrame, text = "Green", width = 7)
        green.bind("<Button-1>", Green.change)
        green.pack(side = LEFT)

class Blue():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "blue"
        FILLED_COLOR_BORDER = "blue"

    def button():
        blue = Button(buttonFrame, text = "Blue", width = 7)
        blue.bind("<Button-1>", Blue.change)
        blue.pack(side = LEFT)

class Yellow():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "yellow"
        FILLED_COLOR_BORDER = "yellow"

    def button():
        yellow = Button(buttonFrame, text = "Yellow", width = 7)
        yellow.bind("<Button-1>", Yellow.change)
        yellow.pack(side = LEFT)

class Red():
    def change(self):
        global FILLED_COLOR_BG
        global FILLED_COLOR_BORDER
        FILLED_COLOR_BG = "red"
        FILLED_COLOR_BORDER = "red"

    def button():
        red = Button(buttonFrame, text = "Red", width = 7)
        red.bind("<Button-1>", Red.change)
        red.pack(side = LEFT)


if __name__ == "__main__" :
    app = Tk()

    #defines global variables to be able to change colors
    FILLED_COLOR_BG = "Black"
    FILLED_COLOR_BORDER = "Black"
    EMPTY_COLOR_BG = "White"
    EMPTY_COLOR_BORDER = "Black"

    #creates buttons used to change colors
    buttonFrame = Frame(app)
    buttonFrame.pack(side = TOP)
        
    Black.button()
    White.button()
    Red.button()
    Orange.button()
    Yellow.button()
    Green.button()
    Blue.button()
    Purple.button()
    Clear.button()
    
    #creates canvas to draw on
    cellGrid = CellGrid(app, 50, 50, 15)
    cellGrid.pack()
    
    app.mainloop()
