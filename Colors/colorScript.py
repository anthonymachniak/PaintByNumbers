def main():
    colorList = ["White", "Black", "Purple", "Orange", "Green", "Blue", "Yellow", "Red"]
    colorClasses = open('colorClasses.txt', 'w')

    for color in colorList:
        colorClasses.write("class " + color + "():\n")
        colorClasses.write("    def change(self):\n")
        colorClasses.write("        global currentColor\n")
        colorClasses.write('        currentColor ="' + color + '"\n')
        colorClasses.write("\n")
        colorClasses.write("    def button():\n")
        colorClasses.write("        " + color.lower() + " = Button(buttonFrame, text = \"" + color + "\", width = 7)\n")
        colorClasses.write("        " + color.lower() + ".bind(\"<Button-1>\", " + color + ".change)\n")
        colorClasses.write("        " + color.lower() + ".pack(side = LEFT)")
        colorClasses.write("\n\n")
    
    colorClasses.close()

main()