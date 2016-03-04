def anagrams(word, words):
    sorted_word = sorted(word)
    return [w for w in words if sorted(w) == sorted_word]

if __name__=='__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
