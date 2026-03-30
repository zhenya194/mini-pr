from PIL import Image, ImageFilter
from funcs import small_blur, average_blur, big_blur
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
    elif command.lower() == "rimage":
        path:str = input("Write absolute path to your image: ")
        effect:str = input("Write effect which you want to do on image: ")
        if effect.lower() == "blur":
            image = average_blur(path)
        image.save(f"image{random.randint(103, 3024)}.png")
