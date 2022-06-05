
from tkinter import *

class GUI:

    def __init__(self):
        # creating a variable for a Tk object
        self.root = Tk() 

        # setting the maze_size variable to a sentinel value, its actual value will be taken via user input using a graphical interface
        self.maze_size = -1

        # setting the title to an appropriate name 
        self.root.title('Pathfinder')

    def main(self):
        # setting the size of the Tk object to the appropriate size
        self.root.geometry("300x130")

        # centering the Tk window so that it appears in the center of the screen 
        self.root.eval('tk::PlaceWindow . center')

        # creating a label containing some text for the 
        maze_generation_label = Label(self.root, text='\nEnter the size of the maze to be generated.\n')

        # adding that particular label to the Tk object
        maze_generation_label.pack()

        # creating a textfield for the user to enter an integer for the size of the maze
        input_maze_size = Entry(self.root, justify='center')

        # adding that particular text field to the Tk object 
        input_maze_size.pack() 

        def when_clicked():
            # taking input of the maze size from the input field 
            self.maze_size = int(input_maze_size.get())

            # closing the Tk object as its purpose of collecting input has been served
            self.root.destroy()

        # creating a button to act as the Submit button once the size of the maze has been loaded into the textfield provided
        submit_button = Button(self.root, text="Submit", command=when_clicked)
        
        # adding that particular button to the Tk object
        submit_button.pack(side = TOP)

        # running the mainloop on the Tk object
        self.root.mainloop()

        # returning the integer collected by the GUI object 
        return self.maze_size