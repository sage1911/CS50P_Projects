from PIL import Image
from PIL import ImageFilter



def main():
    with Image.open("in.jpg") as img:
        rotated = img.rotate(360)
        rotated = img.filter(ImageFilter.FIND_EDGES)
        rotated.save("out.jpg")
 


main()    