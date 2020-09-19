from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser


class menu_class:

    def __init__(self):
        self.frame = None
        self.clr = "light green"
        self.combo = None
        self.color_entry = None
        self.change_color_btn = None
        self.entry = None
        self.entry1 = None
        self.entry2 = None
        self.combo_label = None
        self.red_label = None
        self.green_label = None
        self.blue_label = None
        self.hexcode_label = None
        self.heading_label = None
        self.html_label = None
        self.info_label = None
        self.link_label = None
        self.size_label = None
        self.setting_info1_label = None
        self.setting_info2_label = None

    def getColor(self):
        return self.clr

    def change_component_color(self):
        try:
            self.frame.config(bg=self.getColor())
            self.combo_label.config(bg=self.getColor())
            self.heading_label.config(bg=self.getColor())
            self.info_label.config(bg=self.getColor())
            self.link_label.config(bg=self.getColor())
            self.size_label.config(bg=self.getColor())
            # self.html_label.config(background=self.getColor())
            if self.hexcode_label:
                self.hexcode_label.config(bg=self.getColor())
            elif self.red_label:
                self.red_label.config(bg=self.getColor())
                self.green_label.config(bg=self.getColor())
                self.blue_label.config(bg=self.getColor())
        except:
            messagebox.showerror(title="Input Error", message="Color code is invalid")

    def RGB(self, rgb=(255, 10, 255)):
        self.clr = "#%02x%02x%02x" % rgb
        self.change_component_color()

    def create_menu_frame(self, frame3, menu_obj):
        self.frame = frame3
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.size_label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.getColor())
        self.size_label.pack(pady=10, ipadx=520)
        if menu_obj == "Change Background":
            self.heading_label = Label(frame3, text="Change Background", font=("normal", 20, "underline"),
                                       bg=self.getColor())
            self.heading_label.pack(side=TOP, pady=10)
            self.combo_label = Label(frame3, text="Select the color code type", font=("Verdana", 11),
                                     bg=self.getColor())
            self.combo_label.pack(side=TOP, pady=20)
            self.combo = ttk.Combobox(frame3, state="readonly", value=["RGB value", "Hexcode"])
            self.combo.current(0)
            self.combo.pack(side=TOP)
            self.combo.bind('<<ComboboxSelected>>', lambda g: self.on_select(frame3))
            self.change_color_btn = Button(frame3, text="Change Background Color", cursor="hand2",
                                           command=self.change_background_color)
            self.change_color_btn.pack(side=TOP, pady=30)
            self.info_label = Label(frame3, text="To know how color code works", bg=self.getColor(),
                                    font=("normal", 10))
            self.info_label.place(x=20, y=470)
            self.link_label = Label(frame3, text="click me", fg="blue", cursor="hand2", font=("normal", 10),
                                    bg=self.getColor())
            self.link_label.place(x=200, y=470)
            self.link_label.bind("<Button-1>", lambda c: webbrowser.open_new("https://www.color-hex.com"))
        if menu_obj == "Settings":
            self.setting_info1_label = Label(frame3, text="Setting menu was not implemented ",
                                             font=("normal", 15), bg=self.getColor())
            self.setting_info1_label.pack(side=TOP, pady=100)
            self.setting_info2_label = Label(frame3, text="|@_@|",
                                             font=("normal", 25), bg=self.getColor())
            self.setting_info2_label.pack(side=TOP)

    def change_background_color(self):
        if self.combo.get() == "RGB value":
            if (self.entry is not None and self.entry.get()) and (self.entry1 is not None and self.entry1.get()) and (
                    self.entry2 is not None and self.entry2.get()):
                if int(self.entry.get()) <= 255 and int(self.entry1.get()) <= 255 and int(self.entry2.get()) <= 255:
                    self.RGB((int(self.entry.get()), int(self.entry1.get()), int(self.entry2.get())))
                else:
                    messagebox.showerror(title="Color code error", message="Color code is invalid")
            else:
                messagebox.showerror(title="Input error", message="No input is given")
        elif self.combo.get() == "Hexcode":
            if self.color_entry.get():
                self.clr = self.color_entry.get()
                self.change_component_color()
            else:
                messagebox.showerror(title="Input error", message="No input is given")

    def on_select(self, frame3):
        if self.combo.get() == "RGB value":
            if self.color_entry:
                self.hexcode_label.destroy()
                self.color_entry.destroy()
                self.hexcode_label = None
                self.color_entry = None
            self.change_color_btn.pack_forget()
            self.red_label = Label(frame3, text="Enter the value for Red color", font=("normal", 10),
                                   bg=self.getColor())
            self.red_label.pack(side=TOP, pady=10)
            self.entry = Entry(frame3, width=23, bg="red")
            self.entry.pack(side=TOP)
            self.green_label = Label(frame3, text="Enter the value for Green color", font=("normal", 10),
                                     bg=self.getColor())
            self.green_label.pack(side=TOP, pady=10)
            self.entry1 = Entry(frame3, width=23, bg="green")
            self.entry1.pack(side=TOP)
            self.blue_label = Label(frame3, text="Enter the value for Blue color", font=("normal", 10),
                                    bg=self.getColor())
            self.blue_label.pack(side=TOP, pady=10)
            self.entry2 = Entry(frame3, width=23, bg="blue")
            self.entry2.pack(side=TOP)
            self.change_color_btn.pack(side=TOP, pady=20)

        if self.combo.get() == "Hexcode":
            if self.entry:
                self.red_label.destroy()
                self.entry.destroy()
                self.green_label.destroy()
                self.entry1.destroy()
                self.blue_label.destroy()
                self.entry2.destroy()
            self.change_color_btn.pack_forget()
            self.hexcode_label = Label(frame3, text="Enter the hex code of color", font=("normal", 10),
                                       bg=self.getColor())
            self.hexcode_label.pack(side=TOP, pady=10)
            self.color_entry = Entry(frame3, font=("Verdana", 10), width=17)
            self.color_entry.pack(side=TOP)
            self.change_color_btn.pack(side=TOP, pady=30)
