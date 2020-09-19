# import required package's
from tkinter import *
from PIL import ImageTk, Image
from Frame_3 import Frame3
from Menu_Frame import menu_class


# create a Frame2 class
class Frame2:
    # constructor
    def __init__(self, root):
        self.root = root
        self.m = menu_class()
        self.frame1 = LabelFrame(self.root, bg="light gray", pady=10)
        self.frame1.pack(fill=BOTH, side=TOP)
        # create a frame2 for displaying option buttons
        self.frame2 = LabelFrame(self.root, bg="light gray", width=0, height=520)
        self.frame2.pack(fill=BOTH, side=LEFT, expand=True)
        self.frame3 = LabelFrame(self.root, bg="light green", width=1050, height=520)
        self.frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.Title = Label(self.frame1, text="CONVERTER", font=("times new roman", 20, "bold"), bd=0, fg='blue',
                           bg="light gray", relief=GROOVE)
        self.Title.pack(fill=BOTH, ipady=0)
        # initialize arrow image
        self.R_arr = ImageTk.PhotoImage(Image.open("Right_arrow.png"))
        # create a button1
        self.button1 = Button(self.frame2, bg="light gray", pady=5, text="Image to PDF", font=("Verdana", 15), width=4,
                              bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button1))
        # create a button2
        self.button2 = Button(self.frame2, bg="light gray", pady=5, text="PDF to Text", font=("Verdana", 15), width=4,
                              bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button2))
        # create a button3
        self.button3 = Button(self.frame2, bg="light gray", pady=5, text="Text to PDF", font=("Verdana", 15), width=4,
                              bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button3))
        # create a button4
        self.button4 = Button(self.frame2, bg="light gray", pady=5, text="Mearge PDF", font=("Verdana", 15), width=4,
                              bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button4))
        # create a button5
        self.button5 = Button(self.frame2, bg="light gray", padx=95, pady=5, text="Docx to PDF", font=("Verdana", 15),
                              width=4, bd=1,
                              cursor="hand2", compound=RIGHT, command=lambda: self.add_image(self.button5))
        self.menu_img = ImageTk.PhotoImage(Image.open("menu_dot.png"))
        self.menu_btn = Button(self.frame1, image=self.menu_img, bd=0, command=self.show_on_frame2)
        self.menu_btn.pack(side=LEFT, anchor=S)
        self.menu = Listbox(self.frame2, bg="light gray", width=10, font=("Havetica", 15), selectbackground="#6d6875")
        self.menu_active = False
        self.button_active = True
        self.show_on_frame2()

    def show_on_frame2(self):
        if self.button_active:
            self.menu.destroy()
            self.button1.pack(fill=BOTH, side=TOP)
            self.button2.pack(fill=BOTH, side=TOP)
            self.button3.pack(fill=BOTH, side=TOP)
            self.button4.pack(fill=BOTH, side=TOP)
            self.button5.pack(fill=BOTH, side=TOP)
            self.button_active = False
            self.menu_active = True
        elif self.menu_active:
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
            self.button4.pack_forget()
            self.button5.pack_forget()
            self.button_active = True
            self.menu_active = False
            self.menu = Listbox(self.frame2, bg="light gray", width=22, height=30, bd=0, font=("Havetica", 15),
                                selectbackground="#6d6875")
            self.menu.pack(fill=BOTH, side=TOP)
            menu_list = ["Change Background", "Settings", "Others"]
            for item in menu_list:
                self.menu.insert(END, item)
            self.menu.bind('<Button-1>', lambda a: self.menu_click(self.menu.get(ANCHOR)))

    def menu_click(self, menu_obj):
        if menu_obj == "Change Background":
            if self.frame3:
                self.frame3.pack_forget()
                self.frame3 = LabelFrame(self.root, bg=self.m.getColor(), width=1050, height=520)
                self.m.create_menu_frame(self.frame3, menu_obj)
            else:
                self.frame3 = LabelFrame(self.root, bg=self.m.getColor(), width=1050, height=520)
                self.m.create_menu_frame(self.frame3, menu_obj)
        if menu_obj == "Settings":
            if self.frame3:
                self.frame3.pack_forget()
                self.frame3 = LabelFrame(self.root, bg=self.m.getColor(), width=1050, height=520)
                self.m.create_menu_frame(self.frame3, menu_obj)
            else:
                self.frame3 = LabelFrame(self.root, bg=self.m.getColor(), width=1050, height=520)
                self.m.create_menu_frame(self.frame3, menu_obj)

    # method to create a frame3 by calling Frame3 class
    def create_frame(self, btn):
        # create a instance of Frame3 class
        a = Frame3(self.m)
        # create a frame3 in class Frame2
        self.frame3 = LabelFrame(self.root, bg=self.m.getColor(), width=1050, height=520)
        # self.frame3.pack(side=RIGHT)
        # if button1 clicked call method create_frame1 of class Frame3
        if btn == self.button1:
            a.create_frame1(self.frame3)
        # if button2 clicked call method create_frame2 of class Frame3
        if btn == self.button2:
            a.create_frame2(self.frame3)
        # if button3 clicked call method create_frame3 of class Frame3
        if btn == self.button3:
            a.create_frame3(self.frame3)
        # if button4 clicked call method create_frame4 of class Frame3
        if btn == self.button4:
            a.create_frame4(self.frame3)
        # if button5 clicked call method create_frame5 of class Frame3
        if btn == self.button5:
            a.create_frame5(self.frame3)

    # method to add arrow image to buttons on click of that button
    def add_image(self, btn):

        # if button1 is clicked
        if btn == self.button1:
            # add image on button1
            btn.config(image=self.R_arr, pady=6, padx=60)
            # remove image from other button
            self.button2.config(image="", padx=95, pady=5)
            self.button3.config(image="", padx=95, pady=5)
            self.button4.config(image="", padx=95, pady=5)
            self.button5.config(image="", padx=95, pady=5)
            '''if frame3 exists then first delete that frame
                and call create_frame method to create new frame and pass button1..
                else simply call create_frame method and pass button1'''
            if self.frame3:
                self.frame3.pack_forget()
                self.create_frame(btn)
            else:
                self.create_frame(btn)

        # if button2 is clicked
        if btn == self.button2:
            # add image on button2
            btn.config(image=self.R_arr, pady=6, padx=75)
            # remove image from other button
            self.button1.config(image="", padx=95, pady=5)
            self.button3.config(image="", padx=95, pady=5)
            self.button4.config(image="", padx=95, pady=5)
            self.button5.config(image="", padx=95, pady=5)
            '''if frame3 exists then first delete that frame
                and call create_frame method to create new frame and pass button2..
                else simply call create_frame method and pass button2'''
            if self.frame3:
                self.frame3.pack_forget()
                self.create_frame(btn)
            else:
                self.create_frame(btn)

        # if button3 is clicked
        if btn == self.button3:
            # add image on button3
            btn.config(image=self.R_arr, pady=6, padx=70)
            # remove image from other button
            self.button1.config(image="", padx=95, pady=5)
            self.button2.config(image="", padx=95, pady=5)
            self.button4.config(image="", padx=95, pady=5)
            self.button5.config(image="", padx=95, pady=5)
            '''if frame3 exists then first delete that frame
                and call create_frame method to create new frame and pass button3..
                else simply call create_frame method and pass button3'''
            if self.frame3:
                self.frame3.pack_forget()
                self.create_frame(btn)
            else:
                self.create_frame(btn)

        # if button4 is clicked
        if btn == self.button4:
            # add image on button4
            btn.config(image=self.R_arr, pady=6, padx=70)
            # remove image from other button
            self.button1.config(image="", padx=95, pady=5)
            self.button2.config(image="", padx=95, pady=5)
            self.button3.config(image="", padx=95, pady=5)
            self.button5.config(image="", padx=95, pady=5)
            '''if frame3 exists then first delete that frame
                and call create_frame method to create new frame and pass button4..
                else simply call create_frame method and pass button4'''
            if self.frame3:
                self.frame3.pack_forget()
                self.create_frame(btn)
            else:
                self.create_frame(btn)

        # if button5 is clicked
        if btn == self.button5:
            # add image on button5
            btn.config(image=self.R_arr, pady=6, padx=70)
            # remove image from other button
            self.button1.config(image="", padx=95, pady=5)
            self.button2.config(image="", padx=95, pady=5)
            self.button3.config(image="", padx=95, pady=5)
            self.button4.config(image="", padx=95, pady=5)
            '''if frame3 exists then first delete that frame
                and call create_frame method to create new frame and pass button5..
                else simply call create_frame method and pass button5'''
            if self.frame3:
                self.frame3.pack_forget()
                self.create_frame(btn)
            else:
                self.create_frame(btn)
