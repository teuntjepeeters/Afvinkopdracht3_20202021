from tkinter import *

def mainframe(source,side):
    """This function is used to generate the frame of the calculator"""
    w = Frame(source, borderwidth=5, bd=5, bg="light green")
    w.pack(expand=YES,fill=BOTH, side=side)
    return w

def button(source, side, text, command=None):
    """This function is used to generate buttons"""
    tempobject = Button(source,text=text, command=command)
    tempobject.pack(side=side, expand = YES, fill=BOTH)
    return tempobject


class calculator(Frame):
    """This class is the calculator at it's core
    It has an entry to display the outcome
    It uses for loops and global function to generate locations and buttons
    lambda is used to generate temporary code to make calculations
    in the the eval function is used to run this code, if it is not possible "error" is displayed
    """
    def __init__(self):
        Frame.__init__(self)

        self.pack(expand=YES,fill=BOTH)

        display = StringVar()
        Entry(self, textvariable=display,justify='right', bg="red").pack(side=TOP,expand=YES,fill=BOTH)

        clear = mainframe(self, TOP) #call the 'main frame' to generate space in the pop-up
        button(clear, LEFT, 'Clear', lambda tempobject=display, x='Clear': tempobject.set("")) # button to erase display
        # use lambda to make a temporary function in the function
        for displaynumbers in ("123/", "456*", "789-", "0.+"): #generate all the buttons in a for loop
            buttonframe = mainframe(self,TOP) #call the 'main frame' to generate for every character
            for location in displaynumbers: # for every display location generate a button
                button(buttonframe,LEFT,location,lambda tempobject=display,x=location: tempobject.set(tempobject.get() + x ))

        equalbutton = mainframe(self, TOP) #call the 'main frame' to generate space in the pop-up
        btnequal = button(equalbutton, LEFT, "=")
        btnequal.bind('<ButtonRelease-1>', lambda e, s=self,
                                                  tempobject=display: s.calc(tempobject), '+')


    def calc(self, display):
        """this function is used to set Entry window equal to the display variable to change what is displayed in that window"""
        try:
            display.set(eval(display.get())) # The eval function is used to the lambda function within the program
        # if it is not possible to run a lambda function, perhaps when wrong input is given, the program displays error
        except:
            display.set("ERROR") #if it is not possible to display the value of display, error is displayed


def main():
    """the calculator class is called and mainloop to run the window"""
    calculator().mainloop()


main()
