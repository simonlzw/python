def gen_file(filename):
    lines = []
    with open(filename, mode="r") as fr:
        for item in fr.readlines():
            lines.append(item)
            if len(lines) == 10:
                yield lines
                lines.clear()
            if len(lines) != 0:
                yield lines

if __name__ == '__main__':
    gen = gen_file("data.txt")
    for item in gen:
        print(item)
        print("----------")