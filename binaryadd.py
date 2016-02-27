def add_binary(first, second):
    return "{0:b}".format(first + second)


if __name__=='__main__':
    print(add_binary(1,1))
    print(add_binary(1,0))
    print(add_binary(51,12))
