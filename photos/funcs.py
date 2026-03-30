from PIL import Image, ImageFilter
def small_blur(path):
    image = Image.open(path)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    return image
def average_blur(path):
    image = Image.open(path)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    return image
def big_blur(path):
    image = Image.open(path)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    return image
