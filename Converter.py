# Required package's
from Frame_2 import Frame2


# Class for Converter
class ImageConverter:

    # Constructor
    def __init__(self, root):
        self.root = root
        # set new title for root
        self.root.title("Converter Application")
        # set the geometry for root window
        self.root.geometry("800x600+350+100")
        # create a frame for action performing
        # self.frame3 = LabelFrame(self.root, width=550, height=520)
        # self.frame3.pack(side=RIGHT)
        # call Frame2 class to create frame2 and to display options
        Frame2(self.root)
