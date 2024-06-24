def character_count(word):
    res = dict()

    for char in word:
        res[char] = res.get(char, 0) + 1

    return res

if __name__ == '__main__':
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))