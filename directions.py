def dirReduce(arr):
    result = []
    dir_dict = {k:arr.count(k) for k in arr}
    ns = dir_dict['NORTH'] - dir_dict['SOUTH']
    ew = dir_dict['EAST'] - dir_dict['WEST']
    if ns != 0:
        result += ['NORTH'] * abs(ns) if ns > 1 else ['SOUTH'] * abs(ns)
    if ew != 0:
        result += ['EAST'] * abs(ew) if ew > 0 else ['WEST'] * abs(ns)
    return result

if __name__=='__main__':
    print(dirReduce(['NORTH', 'SOUTH', 'SOUTH', 'NORTH', 'EAST', 'EAST', 'WEST']))
    print(dirReduce(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']))
