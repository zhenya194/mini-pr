en_ru: dict = [
    "a": "ф",
    "b": "и",
    "c": "с",
    "d": "в",
    "e": "у",
    "f": "а",
    "g": "п",
    "h": "р",
    "i": "ш",
    "j": "о",
    "k": "л",
    "l": "д",
    "m": "ь",
    "n": "т",
    "o": "щ",
    "p": "з",
    "q": "й",
    "r": "к",
    "s": "ы",
    "t": "е",
    "u": "г",
    "v": "м",
    "w": "ц",
    "x": "ч",
    "y": "н",
    "z": "я"
]

lang_ru = {"ru", "ру", " Russian", "русский"}
lang_en = {"en", "eng", "English", "англ", "Английский"}

phrase: str = input("Write your phrase(напишите свою фразу): ")
lang: str = input("Write language of your phrase(напишите язык фразы)(en/ru(англ/ру)): ")
final: str = ""

for i in range(len(phrase)):
    for v, k in en_ru:
        if lang in lang_ru:
            if i == k:
                final += v
        elif lang in lang_en:
            if i == v:
                final += k
        else:
            print("Uncorrect lang(неккоректно написан язык).")
            break
