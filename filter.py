from data_transfer import get_all_img_vectors, txt_to_list

if __name__ == "__main__":
    ls = txt_to_list()
    img = get_all_img_vectors()
    print(ls[0])
    print(img[0])
