import itertools

def insert_all_dash(num_in):
    """inserts dash after all odd numbers;
    trims the final dash if the last number is odd"""
    num_list = list(str(num_in))
    odd_indices = [(idx + '-') if int(idx) % 2 != 0 else idx for idx in num_list]
    joined = "".join(odd_indices)
    return joined if joined[-1] != '-' else joined[:-1]

def insert_dash(num):
    """inserts dash between pairs of odd numbers"""
    num_list = list(str(num)+'0')
    a, b = itertools.tee(num_list)
    next(b, None) # offset b by one
    zipped = itertools.izip(a, b)
    odd_dashes = [(a+'-') if int(a)%2 != 0 and int(b)%2 != 0 else a for a,b in zipped]
    return "".join(odd_dashes)

if __name__=='__main__':
    print(insert_dash(454793))
    print(insert_dash(2468))
    print(insert_dash(1357))
