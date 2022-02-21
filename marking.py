import tkinter as tk
import sys
import os

outputDir = ''

def create_button( div, text ):
    bt = tk.Button(div, text=text, bg='red', fg='black', width = 10)
    return bt

def getOutput( ID ):
    ...

def updateOutputs():

    outputList = []
    errList = []

    for root, dirs, files in os.walk(outputDir):
        print( "Dir: ", root)
        for filename in files:
            fileType = os.path.splitext(filename)[1]
            if str(fileType) == '.output':
                outputList.append( filename )
            elif str(fileType) == '.err':
                errList.append( filename )

    return outputList, errList

def main():

    outputList, errList = updateOutputs()
    print( outputList )
    print( errList )


    # draw GUI
    window = tk.Tk()
    window.title('Assignment Marking')
    window_width = 1200
    window_height = 800
    window.geometry('1200x800')
    panel_width = 600
    panel_height = 750
    align_mode = 'nswe'

    div1 = tk.Frame(window,  width=panel_width, height=panel_height, bg='blue')
    div2 = tk.Frame(window,  width=panel_width, height=panel_height, bg='orange')
    div3 = tk.Frame(window,  width=panel_width*2, height=window_height-panel_height, bg='black')

    div1.grid(column=0, row=0)
    div2.grid(column=1, row=0)
    div3.grid(row=1, columnspan=2)

    lbl_1 = tk.Label(window, text="Current: ", bg='white', fg='#263238', font=('Arial', 12), width=20)
    bt1 = create_button( div3, "Run All Assignment" )
    bt2 = create_button( div3, "Open Assignment" )
    bt3 = create_button( div3, "Previous" )
    bt4 = create_button( div3, "Next" )

    lbl_1.grid(column=0, row=1, sticky='w')
    bt1.grid(column=1, row=1, sticky=align_mode)
    bt2.grid(column=2, row=1, sticky=align_mode)
    bt3.grid(column=3, row=1, sticky=align_mode)
    bt4.grid(column=4, row=1, sticky=align_mode)

    window.mainloop()

if __name__ == '__main__':
    try:
        codeDir = sys.argv[1]
        inputDir = sys.argv[2]
    except:
        raise Exception("Usage: python3 marking.py codeDir inputDir")
    main()