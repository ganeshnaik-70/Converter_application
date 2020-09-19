# import required packages
from tkinter import messagebox
from tkinter.filedialog import *
from PIL import ImageTk, Image
from PyPDF2 import PdfFileReader, PdfFileMerger
import pdfplumber
from fpdf import FPDF
import win32com.client
from pathlib import Path


# create a class Frame3
class Frame3:
    def __init__(self, m):
        self.file = None
        self.m = m
        self.img_list = []
        self.final_list = []
        self.file_type = None
        self.text = ''
        self.pdf = FPDF()
        self.merge = PdfFileMerger()
        self.doc = None
        self.btn1 = None
        self.btn2 = None
        self.btn3 = None
        self.label = None
        self.size_label = None
        self.select_img = ImageTk.PhotoImage(Image.open("image_ico.png"))
        self.convert_pdf_img = ImageTk.PhotoImage(Image.open("converter_img.png"))
        self.pdf_img = ImageTk.PhotoImage(Image.open("pdf.png"))
        self.convert_img = ImageTk.PhotoImage(Image.open("convert.png"))
        self.text_img = ImageTk.PhotoImage(Image.open("text.png"))
        self.docx_img = ImageTk.PhotoImage(Image.open("docx.png"))
        self.save_img = ImageTk.PhotoImage(Image.open("save_img.png"))
        self.inside_frame = None

    # create method for displaying frame3
    def create_frame1(self, frame3):
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=40, ipadx=520)
        self.label = Label(frame3, text="Tips: Click on 'Select Image' button and select the Images",
                           font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=25)
        self.btn1 = Button(frame3, text="Select Image", width=60, pady=5, bd=0.5, padx=40, image=self.select_img,
                           compound=RIGHT, cursor="hand2", command=lambda: self.openfile("Image"))
        self.btn1.pack(side=TOP)
        self.btn2 = Button(frame3, text="Convert to Pdf", width=82, pady=5, bd=0.5, padx=29,
                           image=self.convert_pdf_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED,
                           command=lambda: self.convert_img_pdf(self.file))
        self.btn2.pack(side=TOP, pady=30)
        self.btn3 = Button(frame3, text="Save file", width=20, pady=5, bd=0.5, padx=60, image=self.save_img,
                           compound=RIGHT,
                           cursor="hand2", state=DISABLED, command=self.savefile)
        self.btn3.pack(side=TOP)

    # create method for displaying frame3
    def create_frame2(self, frame3):
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.size_label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.size_label.pack(pady=40, ipadx=520)
        self.label = Label(frame3, text="Tips: Click on 'Select Pdf file' button and select the file",
                           font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=25)
        self.btn1 = Button(frame3, text="Select Pdf file", width=80, pady=5, bd=0.5, padx=30, image=self.pdf_img,
                           compound=RIGHT, cursor="hand2", command=lambda: self.openfile("PDF"))
        self.btn1.pack(side=TOP)
        self.btn2 = Button(frame3, text="Convert to Text", width=90, pady=5, bd=0.5, padx=25, image=self.convert_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED,
                           command=lambda: self.convert_pdf_text(self.file))
        self.btn2.pack(side=TOP, pady=30)
        self.btn3 = Button(frame3, text="Save file", width=20, pady=5, bd=0.5, padx=60, image=self.save_img,
                           compound=RIGHT,
                           cursor="hand2", state=DISABLED, command=self.savefile)
        self.btn3.pack(side=TOP)

    # create method for displaying frame3
    def create_frame3(self, frame3):
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.size_label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.size_label.pack(pady=40, ipadx=520)
        self.label = Label(frame3, text="Tips: Click on 'Select Text file' button and select the file",
                           font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=25)
        self.btn1 = Button(frame3, text="Select Text file", width=76, pady=5, bd=0.5, padx=32, image=self.text_img,
                           compound=RIGHT, cursor="hand2", command=lambda: self.openfile("Text"))
        self.btn1.pack(side=TOP)
        self.btn2 = Button(frame3, text="Convert to Pdf", width=80, pady=5, bd=0.5, padx=30, image=self.convert_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED,
                           command=lambda: self.convert_text_pdf(self.file))
        self.btn2.pack(side=TOP, pady=30)
        self.btn3 = Button(frame3, text="Save file", width=20, pady=5, bd=0.5, padx=60, image=self.save_img,
                           compound=RIGHT,
                           cursor="hand2", state=DISABLED, command=self.savefile)
        self.btn3.pack(side=TOP)

    # create method for displaying frame3
    def create_frame4(self, frame3):
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.size_label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.size_label.pack(pady=40, ipadx=520)
        self.label = Label(frame3, text="Tips: Click on 'Select Pdf files' button and select the files",
                           font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=25)
        self.btn1 = Button(frame3, text="Select Pdf files", width=80, pady=5, bd=0.5, padx=30, image=self.pdf_img,
                           compound=RIGHT, cursor="hand2", command=lambda: self.openfile("PDFs"))
        self.btn1.pack(side=TOP)
        self.btn2 = Button(frame3, text="Marge Pdf file", width=78, pady=5, bd=0.5, padx=31, image=self.convert_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED, command=lambda: self.marge_pdf(self.file))
        self.btn2.pack(side=TOP, pady=30)
        self.btn3 = Button(frame3, text="Save file", width=20, pady=5, bd=0.5, padx=60, image=self.save_img,
                           compound=RIGHT,
                           cursor="hand2", state=DISABLED, command=self.savefile)
        self.btn3.pack(side=TOP)

    # create method for displaying frame3
    def create_frame5(self, frame3):
        frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.size_label = Label(frame3, text="", font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.size_label.pack(pady=40, ipadx=520)
        self.label = Label(frame3, text="Tips: Click on 'Select Docx file' button and select the file",
                           font=('times new roman', 13, 'bold'), bg=self.m.getColor())
        self.label.pack(pady=25)
        self.btn1 = Button(frame3, text="Select Docx file", width=100, pady=5, bd=0.5, padx=20, image=self.docx_img,
                           compound=RIGHT, cursor="hand2", command=lambda: self.openfile("Docx"))
        self.btn1.pack(side=TOP)
        self.btn2 = Button(frame3, text="Convert to Pdf", width=84, pady=5, bd=0.5, padx=28, image=self.convert_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED,
                           command=lambda: self.convert_docx_pdf(self.file))
        self.btn2.pack(side=TOP, pady=30)
        self.btn3 = Button(frame3, text="Select path to save", width=124, pady=5, bd=0.5, padx=8, image=self.save_img,
                           compound=RIGHT, cursor="hand2", state=DISABLED, command=self.savefile)
        self.btn3.pack(side=TOP)

    def openfile(self, file_type):
        if file_type == "Image":
            self.file = askopenfilenames(title="Select file", filetypes=(("PNG file", "*.png"), ("JPG files", "*.jpg"),
                                                                         ("bmp files", "*.bmp"), ("GIF files", "*.gif"),
                                                                         ("All file", "*.*")))
        elif file_type == "PDF" or file_type == "PDFs":
            self.file = askopenfilenames(title="Select file", filetypes=(("PDF file", "*.pdf"), ("All file", "*.*")))
        elif file_type == "Text":
            self.file = askopenfilename(title="Select file", filetypes=(("Text file", "*.txt"), ("All file", "*.*")))
        elif file_type == "Docx":
            self.file = askopenfilename(title="Select file",
                                        filetypes=(("Docx file", ("*.docx", "*.doc")), ("All file", "*.*")))
        if self.file != "":
            self.btn2.config(state=NORMAL)
            self.file_type = file_type
            self.label.config(text="Tips: Now click on 'Convert' button to convert the file")

    def convert_img_pdf(self, file_list):
        lenght = len(file_list)
        image_list = []
        self.img_list = []
        self.final_list = []
        for i in range(0, lenght):
            image_list.append("h")
            self.img_list.append("k")
        for i in range(0, lenght):
            image_list[i] = Image.open(file_list[i])
            self.img_list[i] = image_list[i].convert('RGB')
            if i != 0:
                self.final_list.append(self.img_list[i])
        self.btn3.config(state=NORMAL)
        self.label.config(text="Tips: Now click 'Save' button to save the file")
        self.label.pack(pady=25)

    def convert_pdf_text(self, file_dict):
        pdfFileObj = open(file_dict[0], "rb")
        pdfReader = PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        pdf = pdfplumber.open(file_dict[0])
        self.text = ''
        for i in range(num_pages):
            page = pdf.pages[i]
            self.text += page.extract_text()
        if self.text == '':
            messagebox.showerror(title="File error", message="Pdf file format is invalid")
        else:
            self.btn3.config(state=NORMAL)
        pdfFileObj.close()
        pdf.close()
        self.label.config(text="Tips: Now click 'Save' button to save the file")
        self.label.pack(pady=25)

    def convert_text_pdf(self, file_dict):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=11)
        f = open(file_dict, 'r')
        for x in f:
            self.pdf.cell(200, 10, txt=x, ln=1, align='L')
        self.btn3.config(state=NORMAL)
        self.label.config(text="Tips: Now click 'Save' button to save the file")
        self.label.pack(pady=25)

    def marge_pdf(self, file_dict):
        file_dict = list(file_dict)
        try:
            for pdf in file_dict:
                self.merge.append(pdf)
            self.btn3.config(state=NORMAL)
            self.label.config(text="Tips: Now click 'Save' button to save the file")
            self.label.pack(pady=25)
        except:
            messagebox.showerror(title="Selection Error", message="Pdf file is invalid")

    def convert_docx_pdf(self, file_dict):
        word = win32com.client.Dispatch("Word.Application")
        input_path = Path(file_dict).resolve()
        docx_filepath = Path(input_path.resolve())
        self.doc = word.Documents.Open(str(docx_filepath))
        self.btn3.config(state=NORMAL)
        self.label.config(text="Tips: Now click 'Save' button to save the file")
        self.label.pack(pady=25)

    def savefile(self):
        if self.file_type == "Image":
            try:
                untitled_file = asksaveasfilename(title="Save file As", defaultextension=".pdf",
                                                  initialfile="Untitled.pdf",
                                                  filetypes=(("All Files", "*.*"), ("Text Files", ".txt")))
                save_file = untitled_file
                self.img_list[0].save(save_file, save_all=True, append_images=self.final_list)
                self.label.config(text="File saved successfully..")
                self.label.pack(pady=25)
                self.btn2.config(state=DISABLED)
                self.btn3.config(state=DISABLED)
            except:
                messagebox.showerror(title="Path Error", message="Please select a path to save the file")
        elif self.file_type == "PDF":
            try:
                untitled_file = asksaveasfilename(title="Save file As", defaultextension=".txt",
                                                  initialfile="Untitled.txt",
                                                  filetypes=(("All Files", "*.*"), ("Text Files", ".txt")))
                save_file = untitled_file
                f = open(save_file, 'a')
                f.write(self.text)
                f.close()
                self.label.config(text="File saved successfully..")
                self.label.pack(pady=25)
                self.btn2.config(state=DISABLED)
                self.btn3.config(state=DISABLED)
            except:
                messagebox.showerror(title="Path Error", message="Please select a path to save the file")
        elif self.file_type == "Text":
            try:
                untitled_file = asksaveasfilename(title="Save file As", defaultextension=".pdf",
                                                  initialfile="Untitled.pdf",
                                                  filetypes=(("All Files", "*.*"), ("Text Files", ".txt")))
                save_file = untitled_file
                self.pdf.output(save_file)
                self.label.config(text="File saved successfully..")
                self.label.pack(pady=25)
                self.btn2.config(state=DISABLED)
                self.btn3.config(state=DISABLED)
            except:
                messagebox.showerror(title="Path Error", message="Please select a path to save the file")
        elif self.file_type == "PDFs":
            try:
                untitled_file = asksaveasfilename(title="Save file As", defaultextension=".pdf",
                                                  initialfile="Untitled.pdf",
                                                  filetypes=(("All Files", "*.*"), ("Text Files", ".txt")))
                save_file = untitled_file
                self.merge.write(save_file)
                self.merge.close()
                self.label.config(text="File saved successfully..")
                self.label.pack(pady=25)
                self.btn2.config(state=DISABLED)
                self.btn3.config(state=DISABLED)
            except:
                messagebox.showerror(title="Path Error", message="Please select a path to save the file")
        elif self.file_type == "Docx":
            try:
                untitled_file = asksaveasfilename(title="Save file As", defaultextension=".pdf",
                                                  initialfile="Untitled.pdf",
                                                  filetypes=(("All Files", "*.*"), ("Pdf Files", ".pdf")))
                wdFormatPDF = 17
                output_path = Path(untitled_file).resolve()
                if output_path:
                    assert str(output_path).endswith(".pdf")
                final_path = output_path
                pdf_filepath = Path(final_path.resolve())
                self.doc.SaveAs(str(pdf_filepath), FileFormat=wdFormatPDF)
                self.doc.Close()
                self.label.config(text="File saved successfully..")
                self.label.pack(pady=25)
                self.btn2.config(state=DISABLED)
                self.btn3.config(state=DISABLED)
            except:
                messagebox.showerror(title="Path Error", message="Please select a path to save the file")
        else:
            messagebox.showerror(title="File Error", message="Please select the file to convert")
