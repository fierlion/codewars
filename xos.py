def xo(string_in):
    return string_in.count('x') == string_in.count('o')

if __name__=='__main__':
    print(xo('xo'))
    print(xo('xo0'))
    print(xo('xxxoo'))
