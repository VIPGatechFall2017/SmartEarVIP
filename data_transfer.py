from PIL import Image
from resizeimage import resizeimage
import os
import numpy as np
from scipy import misc
import glob
import cv2
import csv

def mov_to_img(file):
    vidcap = cv2.VideoCapture(file);
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print('Read a new frame: ', count, success)
        cv2.imwrite("image/frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1

def txt_to_csv(file_title):
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file = open(file_title, 'r')
        for line in file.readlines():
            st = line.split(", ")[1].split(";")[0]
            ls = st.split(" ")
            writer.writerow(ls)

def txt_to_list(file_title):
    file = open(file_title, "r")
    ls = list()
    for line in file.readlines():
        st = line.split(", ")[1].split(";")[0]
        ls.append(st.split(" "))
    return ls

def resize_img(img):
    # print(img[img.index("_") + 1:img.index(".jpg")])
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [28, 28])
            title = img.split("\\")
            title = title[len(title) - 1]
            cover.save("resize/" + title, image.format)
            print("resized", title)

def resize_all_img():
    for file in glob.glob("./image/*.jpg"):
        resize_img(file)

def get_file_number(file):
    return file[file.index("_") + 1 : file.index(".png")]

def get_img_vector(file):
    ls = misc.imread(file, flatten=True)
    return [item for sublist in ls for item in sublist]

def get_all_img_vectors():
    for file in glob.glob("./image/*.jpg"):
        ls.append(get_img_vector(file))
    return ls

def img_to_csv():
    with open('hand.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for file in glob.glob("./resize/*.jpg"):
            # img = get_img_vector(file)
            ls = get_img_vector(file)
            writer.writerow(ls)


if __name__ == "__main__":
    FILE = "data.txt"
    VID_FILE = 'hand.mov'
    # mov_to_img(VID_FILE)
    # txt_to_csv(FILE)
    # resize_all_img()
    img_to_csv()
