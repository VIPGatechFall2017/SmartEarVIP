from PIL import Image
#from resizeimage import resizeimage
import os
import numpy as np
from scipy import misc
import glob
import matplotlib.pyplot as plt

def txt_to_list(file_title):
    file = open(file_title, "r")
    ls = list()
    for line in file.readlines():
        st = line.split(", ")[1].split(";")[0]
        ls.append(int((st.split(" "))[2]))
    return ls

def filterIndex(file_title):
    ls = txt_to_list(file_title)
    #print (ls)
    #print(na)
    index = sorted(range(len(ls)),key=lambda x:ls[x])
    #print(max(index)) #--7140
    #print (min(index)) #--0
    filterind = []
    for i in range(1499,len(index)-300):
       filterind.append(index[i])
    return filterind

filterind = filterIndex("Data.txt")
print (filterind)
