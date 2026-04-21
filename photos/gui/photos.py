from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFilter
import os
import random
import webbrowser

app = Tk()

def generate():
    effect = style.get()
    image = Image.open(path.get())
    if effect.lower() == "blur":
        for i in range(5):
            image = image.filter(ImageFilter.BLUR)
    elif effect.lower() == "white contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif effect.lower() == "canvas":
        for i in range(8):
            image = image.filter(ImageFilter.DETAIL)
    elif effect.lower() == "onboard":
        image = image.filter(ImageFilter.EMBOSS)
    else:
        return None
    image.save(f"image{random.randint(103, 30247)}.png")
    messagebox.showinfo(title="Status", message="Generated")
    
def help():
    doc = os.path.abspath("../index.html")
    webbrowser.open(f"file://{doc}")
    print("Help document had opened in your browser.")

app["bg"] = "#6B6B6B"
app.title("Photos GUI")
app.geometry("400x380")

app.resizable(width=False, height=False)

canvas = Canvas(app, height=400, width=380)
canvas.pack()

frame = Frame(app, bg="#d1d1d1")
frame.place(relwidth=1, relheight=1)

generate_btn = Button(frame, text="Generate", bg="#60ed53", command=generate)
help_btn = Button(frame, text="Help", bg="#f0b4b4", command=help)

text_path = Label(frame, text="Path to image:", bg="gray") # font=40
text_style = Label(frame, text="Style for image:", bg="gray") # font=40

path = Entry(frame, bg="white")
style = Entry(frame, bg="white")

text_path.pack(pady=5)
path.pack(pady=10)
text_style.pack(pady=5)
style.pack(pady=10)
generate_btn.pack(pady=10)
help_btn.pack(pady=12)

app.mainloop()
