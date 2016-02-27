import math

def triangular_range(start, stop):
    result_dict = {}
    # stop at the triangle root
    square_stop = int(math.sqrt(8 * stop) // 2) + 1
    _triangular_range(square_stop, start, stop, result_dict)
    return result_dict

def _triangular_range(start, func_start, func_stop, result):
    if start == 0:
        return 0
    else:
        this_result = _triangular_range(start -1, func_start, func_stop, result) + start
        if this_result >= func_start and this_result <= func_stop:
            result[start] = this_result
        return this_result

if __name__=='__main__':
    print triangular_range(1, 3)
    print triangular_range(5, 16)
