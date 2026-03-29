from PIL import Image, ImageFilter
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
    elif command.lower() == "rimage":
        path:str = str(input("Write absolute path to your image:"))
        image = Image.open(path)
        image = image.filter(ImageFilter.BLUR)
        image = image.filter(ImageFilter.BLUR)
        image = image.filter(ImageFilter.BLUR)
        image = image.filter(ImageFilter.BLUR)
        image.show()
