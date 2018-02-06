def main():
    colorList = ["Red", "DodgerBlue", "Yellow", "Black", "Tan1", "Brown", "Sienna4"]
    colorClasses = open('colorClasses.txt', 'w')

    for color in colorList:
        width = len(color) + 4
        colorClasses.write("class " + color + "():\n")
        colorClasses.write("    def change(self):\n")
        colorClasses.write("        global currentColor\n")
        colorClasses.write('        currentColor ="' + color + '"\n')
        colorClasses.write("\n")
        colorClasses.write("    def button():\n")
        colorClasses.write("        " + color.lower() + " = Button(buttonFrame, text = \"" + color + "\", width = " + str(width) + ")\n")
        colorClasses.write("        " + color.lower() + ".bind(\"<Button-1>\", " + color + ".change)\n")
        colorClasses.write("        " + color.lower() + ".pack(side = LEFT)")
        colorClasses.write("\n\n")
    
    colorClasses.close()

main()