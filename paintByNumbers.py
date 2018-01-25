from tkinter import *

#currentColor identifies the state for the color being drawn on cells. Default is 'black'.
currentColor = "Black"

class Cell():
    def __init__(self, master, x, y, size, color):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        
    def draw(self, color):
        self.color = color
        """ order to the cell to draw its representation on the canvas """
        if self.color == "Clear":
            FILLED_COLOR_BG = "White"
            FILLED_COLOR_BORDER = "Black"
        else:
            FILLED_COLOR_BG = self.color
            FILLED_COLOR_BORDER = self.color
        xmin = self.abs * self.size
        xmax = xmin + self.size
        ymin = self.ord * self.size
        ymax = ymin + self.size

        self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = FILLED_COLOR_BG, outline = FILLED_COLOR_BORDER)


class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        #creation of grid. rowNumber and columnNumber are inputs from main() statement
        self.grid = []
        for row in range(rowNumber):
            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize, "Clear"))
            self.grid.append(line)
        self.draw()

        #button binding
        self.bind("<Button-1>", self.handleMouseClick)  
        self.bind("<B1-Motion>", self.handleMouseClick)
        
    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw("Clear")

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        global currentColor
        cell.draw(currentColor)

#Removes all color from the frame
class FullClear():
    def change(self):
        global cellGrid
        cellGrid.destroy()
        cellGrid = CellGrid(app, 50, 50, 15)
        cellGrid.pack()

    def button():
        fullClear = Button(fullClearButtonFrame, text = "Full Clear", width = 10)
        fullClear.bind("<Button-1>", FullClear.change)
        fullClear.pack()    

#Clears cell of any color
class Eraser():
    def change(self):
        global currentColor
        currentColor ="Clear"

    def button():
        eraser = Button(buttonFrame, text = "Eraser", width = 7)
        eraser.bind("<Button-1>", Eraser.change)
        eraser.pack(side = LEFT)

#Each color has a class so that colors can be added or removed more easily
class White():
    def change(self):
        global currentColor
        currentColor ="White"

    def button():
        white = Button(buttonFrame, text = "White", width = 7)
        white.bind("<Button-1>", White.change)
        white.pack(side = LEFT)

class Black():
    def change(self):
        global currentColor
        currentColor ="Black"

    def button():
        black = Button(buttonFrame, text = "Black", width = 7)
        black.bind("<Button-1>", Black.change)
        black.pack(side = LEFT)

class Purple():
    def change(self):
        global currentColor
        currentColor ="Purple"

    def button():
        purple = Button(buttonFrame, text = "Purple", width = 7)
        purple.bind("<Button-1>", Purple.change)
        purple.pack(side = LEFT)

class Orange():
    def change(self):
        global currentColor
        currentColor ="Orange"

    def button():
        orange = Button(buttonFrame, text = "Orange", width = 7)
        orange.bind("<Button-1>", Orange.change)
        orange.pack(side = LEFT)

class Green():
    def change(self):
        global currentColor
        currentColor ="Green"

    def button():
        green = Button(buttonFrame, text = "Green", width = 7)
        green.bind("<Button-1>", Green.change)
        green.pack(side = LEFT)

class Blue():
    def change(self):
        global currentColor
        currentColor ="Blue"

    def button():
        blue = Button(buttonFrame, text = "Blue", width = 7)
        blue.bind("<Button-1>", Blue.change)
        blue.pack(side = LEFT)

class Yellow():
    def change(self):
        global currentColor
        currentColor ="Yellow"

    def button():
        yellow = Button(buttonFrame, text = "Yellow", width = 7)
        yellow.bind("<Button-1>", Yellow.change)
        yellow.pack(side = LEFT)

class Red():
    def change(self):
        global currentColor
        currentColor ="Red"

    def button():
        red = Button(buttonFrame, text = "Red", width = 7)
        red.bind("<Button-1>", Red.change)
        red.pack(side = LEFT)


if __name__ == "__main__" :
    app = Tk()

    #creates buttons used to change colors
    buttonFrame = Frame(app)
    buttonFrame.pack(side = TOP)
    fullClearButtonFrame = Frame(app)
    fullClearButtonFrame.pack(side = BOTTOM)

    Black.button()
    White.button()
    Red.button()
    Orange.button()
    Yellow.button()
    Green.button()
    Blue.button()
    Purple.button()
    Eraser.button()
    FullClear.button()
    
    #creates canvas to draw on
    #if CellGrid input changes, make sure to change FullClear class
    cellGrid = CellGrid(app, 50, 50, 15)
    cellGrid.pack()
    
    app.mainloop()