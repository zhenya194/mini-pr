from PIL import Image, ImageFilter
import random
import webbrowser
import os
while True:
    command:str = str(input("Write a command(help for help): "))
    if command.lower() == "help":
        try:
            doc = os.path.abspath("index.html")
            webbrowser.open(f"file://{doc}")
            print("Help document had opened in your browser.")
        except:
            print("Error: help document hadn't opened.")
    elif command.lower() == "exit":
        break
    elif command.lower() == "image":
        path:str = input("Write absolute path to your image: ")
        effect:str = input("Write effect which you want to do on image: ")
        image = Image.open(path)
        if effect.lower() == "blur":
            image = image.filter(ImageFilter.BLUR)
            image = image.filter(ImageFilter.BLUR)
            image = image.filter(ImageFilter.BLUR)
            image = image.filter(ImageFilter.BLUR)
            image = image.filter(ImageFilter.BLUR)
        elif effect.lower() == "white contour":
            image = image.filter(ImageFilter.CONTOUR)
        image.save(f"image{random.randint(103, 30247)}.png")
