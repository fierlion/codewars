def f(n, m):
    return sum(range(1, m)) * (n//m) + sum(range(1, (n%m)+1))
if __name__=='__main__':
    print(f(99832618, 17230429))
