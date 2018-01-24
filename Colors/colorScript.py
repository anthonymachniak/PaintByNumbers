def main():
    colorList = ["White", "Black", "Purple", "Orange", "Green", "Blue", "Yellow", "Red"]
    colorClasses = open('colorClasses.txt', 'w')

    for color in colorList:
        colorClasses.write("class " + color + "():\n")
        colorClasses.write("    def change(self):\n")
        colorClasses.write("        global FILLED_COLOR_BG\n")
        colorClasses.write("        global FILLED_COLOR_BORDER\n")
        colorClasses.write("        FILLED_COLOR_BG = \"" + color.lower() + "\"\n")
        colorClasses.write("        FILLED_COLOR_BORDER = \"" + color.lower() + "\"\n")
        colorClasses.write("\n")
        colorClasses.write("    def button():\n")
        colorClasses.write("        " + color.lower() + " = Button(app, text = \"" + color + "\")\n")
        colorClasses.write("        " + color.lower() + ".bind(\"<Button-1>\", " + color + ".change)\n")
        colorClasses.write("        " + color.lower() + ".pack()")
        colorClasses.write("\n\n")
    
    
    colorClasses.close()
    

main()