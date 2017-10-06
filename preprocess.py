
def read_file(file_title):
    file = open(file_title, "r")
    ls = list()
    for line in file.readlines():
        st = line.split(", ")[1].split(";")[0]
        ls.append(st.split(" "))
    return ls
if __name__ == "__main__":
    FILE = "data.txt"
    ls = read_file(FILE)
    for line in ls[0:10]:
        print(line)