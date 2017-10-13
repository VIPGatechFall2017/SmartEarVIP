from PIL import Image
from resizeimage import resizeimage
import os
import numpy as np
from scipy import misc
import glob


def txt_to_list():
    file_title = "data.txt"
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

def resize_all_img():
    for file in os.listdir():
        if file.endswith('png'):
            resize_img(file)

def get_file_number(file):
    return file[file.index("_") + 1 : file.index(".png")]

def get_img_vector(file):
    ls = misc.imread(file, flatten=True)
    return [item for sublist in ls for item in sublist]

def get_all_img_vectors():
    ls = list()
    for file in glob.glob("./image/*.png"):
        ls.append(get_img_vector(file))
    return ls

if __name__ == "__main__":
    ls = txt_to_list()
    img = get_all_img_vectors()
