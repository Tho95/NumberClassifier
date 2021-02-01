# this function ignores the greyscale of the input numbers and turns everything that is grey to black

def toBlack(x_train):
    print("hello")
    for number in range(len(x_train)):
        for row in range(28):
            for x in range(28):
                if x_train[number][row][x] !=0:
                    x_train[number][row][x] = 1
    print("hello")
    return x_train