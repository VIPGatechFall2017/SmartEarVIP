from data_transfer import get_all_img_vectors, txt_to_list
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ls = txt_to_list()
    # img = get_all_img_vectors()

    total = []
    for i in range(10):
        total.append(0)
    for vector in ls:
        ring = vector[3]
        ring = int(int(ring) / 10)
        total[ring] += 1

    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = total

    print(y)

    plt.bar(x, y)
    plt.show()
