# this function ignores the greyscale of the input numbers and turns everything that is grey to black


def toBlack(x_data):

    for number in range(len(x_data)):
        for row in range(28):
            for x in range(28):
                if x_data[number][row][x] !=0:
                    x_data[number][row][x] = 1
    print("greyscale done")

    return x_data