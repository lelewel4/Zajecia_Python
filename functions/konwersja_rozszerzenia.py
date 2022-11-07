from PIL import Image

def convert_jpg_to_png(path:str):
    im1 = Image.open(path)
    im1.save(path[:-4]+'.png')              #usuniecie '.jpg' i dodanie '.png'

