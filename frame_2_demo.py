from tkinter import *
from PIL import Image, ImageTk


class frame2_menu:
    def __init__(self, win):
        self.root = win
        self.root.geometry("800x600+500+100")
        self.frame1 = LabelFrame(self.root, bg="light gray", pady=10)
        self.frame1.pack(fill=BOTH, side=TOP)
        self.Title = Label(self.frame1, text="CONVERTER", font=("times new roman", 20, "bold"), bd=0, fg='blue',
                           bg="light gray", relief=GROOVE)
        self.Title.pack(fill=BOTH, ipady=0)
        # create a frame2 for displaying option buttons
        self.frame2 = LabelFrame(self.root, bg="light gray", width=550, height=520)
        self.frame2.pack(fill=BOTH, side=LEFT, expand=True)
        self.button1 = Button(self.frame2, bg="light gray", pady=5, text="Image to PDF", font=("Verdana", 15), width=4,
                              bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button1))
        # self.button1.pack(fill=BOTH, side=TOP)
        self.frame3 = LabelFrame(self.root, bg="light green", width=300, height=520)
        self.frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.menu_img = ImageTk.PhotoImage(Image.open("menu_dot.png"))
        self.menu_btn = Button(self.frame1, image=self.menu_img, bd=0, command=self.popup_menu)
        self.menu_btn.pack(side=LEFT, anchor=S)
        self.menu = Listbox(self.frame2, bg="light gray", width=10, font=("Havetica", 15), selectbackground="#6d6875")
        self.menu_active = False

    def popup_menu(self):
        if not self.menu_active:
            self.menu.pack(fill=BOTH, side=TOP)
            self.menu_active = True
            menu_list = ["Change background", "Settings", "Others"]
            for item in menu_list:
                self.menu.insert(END, item)
            self.menu.bind('<Double-1>', self.show)

    def show(self, e):
        pass


root = Tk()
frame2_menu(root)
root.mainloop()
