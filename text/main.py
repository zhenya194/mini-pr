while True:
    text:str = input("Write your text: ")
    if text.lower() == "exit" or text.lower() == "stop":
        break
    style:str = input("Which style do you want to do on text(lower or upper): ")
    if style.lower() == "exit" or style.lower() == "stop":
        break
    if style.lower() == "lower":
        print(f"\n\n{text.lower()}\n")
    elif style.lower() == "upper":
        print(f"\n\n{text.upper()}\n")
    else:
        print("Style is not correct")
        continue
