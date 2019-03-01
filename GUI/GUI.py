from tkinter import *
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog

import sys
FREECADPATH = 'C:/Users/Yuan/Anaconda2/pkgs/freecad-0.18b0-py36ha567227_4/Library/bin' # path to your FreeCAD.so or FreeCAD.dll file
sys.path.append(FREECADPATH)

import FreeCAD as App
import Part
import FreeCADGui as Gui
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    def import_fcstd(filename):
        import FreeCAD

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="File", command=self.client_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        print()
#ftypes = [('Python files', '*.py'), ('All files', '*')]
    #dlg = filedialog.Open(self, filetypes=ftypes)
    #fl = dlg.show()

    #if fl != '':





# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

# creation of an instance
app = Window(root)
Gui.showMainWindow()
myDocument = App.newDocument("Document Name")
App.ActiveDocument = myDocument
Gui.ActiveDocument = myDocument

myPart = myDocument.addObject("Part::Feature", "myPartName")
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
Part.show(cube)
# Gui.ActiveDocument.activeView().viewAxometric()
# Gui.ActiveDocument.activeView().fitAll()
Gui.ActiveDocument.recompute()
print(myDocument)
# mainloop
root.mainloop()

