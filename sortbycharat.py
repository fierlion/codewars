def sort_it(list_, n):
    """sorts a str formatted list of words
    by the character at position n"""
    word_list = list_.split(', ')
    word_list.sort(key=lambda x: x[n-1])
    return ', '.join(word_list)

if __name__=='__main__':
    print(sort_it('bill, bell, ball, bull', 2))
    print(sort_it('cat, dog, eel, bee', 3))
