import collections
def find_it(seq):
    for k,v in collections.Counter(seq).items():
        if v % 2 != 0:
            return k

if __name__=='__main__':
    print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

