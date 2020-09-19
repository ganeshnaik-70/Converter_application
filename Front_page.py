from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Converter
from PIL import ImageTk, Image


class Front_page:
    def __init__(self, root):
        self.root = root
        # set the size of the window
        self.root.geometry("800x600+350+100")
        # set the title of the window
        self.root.title("Converter Application")
        # initialize and load icon for root window
        self.icon = ImageTk.PhotoImage(Image.open("icon_pic.png"))
        self.root.iconphoto(False, self.icon)
        # create a frame to put the widgets
        self.main_frame1 = LabelFrame(self.root, width=800, height=600, bg="gray", bd=0)
        self.main_frame1.pack(fill=BOTH, expand=True)
        # create a label to give some padding
        self.label = Label(self.main_frame1, text="", bg="gray")
        self.label.pack(pady=20)
        # load the background image using label
        self.fil = ImageTk.PhotoImage(Image.open("Icon2.png"))
        self.ico_lab = Label(self.main_frame1, image=self.fil, bg="gray")
        self.ico_lab.pack()
        # label for displaying the heading
        self.main_label = Label(self.main_frame1, text="Converter...", font=("Verdana", 45, "bold"), fg="blue",
                                bg="gray")
        self.main_label.pack()
        # create a progress bar
        self.progres_bar = ttk.Progressbar(self.main_frame1, mode="indeterminate", length=300, orient=HORIZONTAL)
        self.progres_bar.pack(pady=10)

    # method to start the progress bar
    def loading_bar(self):
        self.progres_bar.start(5)
        self.progres_bar.after(3000, lambda: self.convert())

    # function for converter
    def convert(self):
        self.main_frame1.pack_forget()
        Converter.ImageConverter(self.root)

    # method for exit
    def exit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit\t\t"):
            self.root.destroy()


win = Tk()
# create a instance of class Front_page
a = Front_page(win)
a.loading_bar()
# check if exit button is clicked
win.protocol('WM_DELETE_WINDOW', a.exit)
win.mainloop()
