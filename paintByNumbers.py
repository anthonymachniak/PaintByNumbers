from tkinter import *
from numberList import numberList

#currentColor identifies the state for the color being drawn on cells. Default is 'black'.
currentColor = "Black"

class Cell():
    def __init__(self, master, x, y, size, color, colorNumber):
        self.master = master
        self.x = x
        self.y = y
        self.size= size
        self.colorNumber = colorNumber
        
    def draw(self, color):
        self.color = color

        xmin = self.x * self.size
        xmax = xmin + self.size
        ymin = self.y * self.size
        ymax = ymin + self.size

        if self.color == "Clear":
            cellBG = "White"
            cellBorder = "Black"
            
            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = cellBG, outline = cellBorder)
            self.master.create_text((xmin+5, ymin+1), anchor = NW, text = self.colorNumber)
        else:
            cellBG = self.color
            cellBorder = self.color
            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = cellBG, outline = cellBorder)


class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize
        defaultColor = "Clear"

        #create grid and initialize objects
        self.grid = []
        listCount = 0
        for row in range(rowNumber):
            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize, defaultColor, numberList[listCount]))
                listCount += 1
            self.grid.append(line)
        
        #draw cells
        for row in self.grid:
            for cell in row:
                cell.draw(defaultColor)

        #button binding
        self.bind("<Button-1>", self.handleMouseClick)  
        self.bind("<B1-Motion>", self.handleMouseClick)

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
        cellGrid = CellGrid(app, 20, 20, 15)
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
class Red():
    def change(self):
        global currentColor
        currentColor ="Red"

    def button():
        red = Button(buttonFrame, text = "Red - 2", width = 7)
        red.bind("<Button-1>", Red.change)
        red.pack(side = LEFT)

class DodgerBlue():
    def change(self):
        global currentColor
        currentColor ="DodgerBlue"

    def button():
        dodgerblue = Button(buttonFrame, text = "Dodger Blue - 3", width = 15)
        dodgerblue.bind("<Button-1>", DodgerBlue.change)
        dodgerblue.pack(side = LEFT)

class Yellow():
    def change(self):
        global currentColor
        currentColor ="Yellow"

    def button():
        yellow = Button(buttonFrame, text = "Yellow - 4", width = 10)
        yellow.bind("<Button-1>", Yellow.change)
        yellow.pack(side = LEFT)

class Black():
    def change(self):
        global currentColor
        currentColor ="Black"

    def button():
        black = Button(buttonFrame, text = "Black - 1", width = 9)
        black.bind("<Button-1>", Black.change)
        black.pack(side = LEFT)

class Tan1():
    def change(self):
        global currentColor
        currentColor ="Tan1"

    def button():
        tan1 = Button(buttonFrame, text = "Tan - 5", width = 7)
        tan1.bind("<Button-1>", Tan1.change)
        tan1.pack(side = LEFT)

class Brown():
    def change(self):
        global currentColor
        currentColor ="Brown"

    def button():
        brown = Button(buttonFrame, text = "Brown - 6", width = 9)
        brown.bind("<Button-1>", Brown.change)
        brown.pack(side = LEFT)

class Sienna4():
    def change(self):
        global currentColor
        currentColor ="Sienna4"

    def button():
        sienna4 = Button(buttonFrame, text = "Sienna - 7", width = 10)
        sienna4.bind("<Button-1>", Sienna4.change)
        sienna4.pack(side = LEFT)


if __name__ == "__main__" :
    app = Tk()

    #creates buttons used to change colors
    buttonFrame = Frame(app)
    buttonFrame.pack(side = TOP)
    fullClearButtonFrame = Frame(app)
    fullClearButtonFrame.pack(side = BOTTOM)

    Black.button()
    Red.button()
    DodgerBlue.button()
    Yellow.button()
    Tan1.button()
    Brown.button()
    Sienna4.button()
    Eraser.button()
    FullClear.button()
    
    #creates canvas to draw on
    #if CellGrid input changes, make sure to change FullClear class
    cellGrid = CellGrid(app, 20, 20, 15)
    cellGrid.pack()
    
    app.mainloop()