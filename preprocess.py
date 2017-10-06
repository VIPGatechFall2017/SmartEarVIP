from PIL import Image
from resizeimage import resizeimage
import os

def txt_to_list(file_title):
    file = open(file_title, "r")
    ls = list()
    for line in file.readlines():
        st = line.split(", ")[1].split(";")[0]
        ls.append(st.split(" "))
    return ls

def resize_img(img):
    print(img[img.index("_") + 1:img.index(".png")])
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [28, 28])
            cover.save("./resize/" + img, image.format)

def get_file_number(file):
    return file[file.index("_") + 1 : file.index(".png")]

def all_img():
    for file in os.listdir():
        if file.endswith('png'):
            resize_img(file)

if __name__ == "__main__":
    FILE = "data.txt"
    ls = txt_to_list(FILE)
    all_img()
