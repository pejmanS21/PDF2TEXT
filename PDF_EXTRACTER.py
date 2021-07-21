from tkinter import filedialog
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
root = Tk()

canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)

# logo
logo = ImageTk.PhotoImage(Image.open("12.ico"))
logo_lable = Label(image=logo)
logo_lable.grid(row=0, column=1)

# instructions
instructions = Label(root, text="select a PDF file to extract", font="Helvetica")
instructions.grid(columnspan=3, column=0, row=1)

# Button function


def open_file():
    browse_text.set("Loading ...")
    pdf_file = askopenfile(parent=root, mode='rb', title="Select a file", filetype=[("PDF file", "*.pdf")])
    if pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page_file = read_pdf.getPage(0)
        page_content = page_file.extractText()
        
        # show Text
        text_box = Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=4)
        browse_text.set("Browse")



# BrowseButton
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font="Helvetica", bg="black", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = Canvas(root, width=600, height=250)
canvas.grid(columnspan=4)


root.mainloop()
