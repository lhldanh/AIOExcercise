def max_kernel(lst, k):
    res = []
    for i in range(len(lst) - k + 1):
        res.append(max(lst[i:i+k]))
    return res

if __name__ == '__main__':
    assert max_kernel ([3 , 4 , 5 , 1 , -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3
    print(max_kernel(num_list , k))