from PIL import Image
from resizeimage import resizeimage
import os
import numpy as np
from scipy import misc
import glob
import cv2
import csv
from operator import itemgetter

def mov_to_img(file):
    vidcap = cv2.VideoCapture(file);
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        if not success:
            print('Failed reading a new frame: ', count)
            continue
        elif count % 100 == 0:
            print('Reading new frame:', count)
        cv2.imwrite("./image/frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1
    print('Read', count, 'images!')


def txt_to_csv(file_title):
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file = open(file_title, 'r')
        for line in file.readlines():
            st = line.split(", ")[1].split(";")[0]
            ls = st.split(" ")
            writer.writerow(ls)
    print('Finished cleaning data.txt to CSV')

def txt_to_list(file_title):
    file = open(file_title, "r")
    ls = list()
    for line in file.readlines():
        st = line.split(", ")[1].split(";")[0]
        ls.append(st.split(" "))
    return ls

def resize_img(img, size):
    # print(img[img.index("_") + 1:img.index(".jpg")])
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [size, size])
            title = img.split("\\")
            title = title[len(title) - 1]
            cover.save("./resize/" + title, image.format)

def resize_all_img(size):
    for file in glob.glob("./image/*.jpg"):
        resize_img(file, size)
    print("Finished resizing images")

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
        images = []
        for file in glob.glob("./resize/*.jpg"):
            name = str(file)
            name = name[name.index("frame") + len("frame") : name.index(".jpg")]
            number = float(name)
            images.append((number, file))
        images.sort(key=lambda x: x[0])
        for number, file in images:
            ls = get_img_vector(file)
            writer.writerow(ls)
    print('Finished transferring resized images to CSV')

if __name__ == "__main__":
    FILE = "data.txt"
    VID_FILE = 'hand.mov'
    SIZE = 30
    os.makedirs('./image', exist_ok=True)
    os.makedirs('./resize', exist_ok=True)
    # mov_to_img(VID_FILE)
    resize_all_img(SIZE)
    img_to_csv()
    # txt_to_csv(FILE)
