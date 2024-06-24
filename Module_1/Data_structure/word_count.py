def count_word(file_path):
    fh = open(file_path, 'r')
    data = fh.read()
    data = data.lower()
    data = data.split()
    
    res = dict()
    for word in data:
        res[word] = res.get(word, 0) + 1
    
    return res

file_path = ('Module_1\Data_structure\P1_data.txt')
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])