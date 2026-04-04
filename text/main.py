while True:
    text:str = input("Write your text: ")
    style:str = input("Which style do you want to do on text(lower or upper): ")
    if style.lower() == "lower":
        print(f"\n\n{text.lower()}\n")
        break
    elif style.lower() == "upper":
        print(f"\n\n{text.upper()}\n")
        break
    else:
        print("Style is not correct")
        continue
