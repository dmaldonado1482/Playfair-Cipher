from itertools import zip_longest


def create_matrix(key):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix_str = key.replace(" ", "") + alphabet
    matrix_list = list(matrix_str.lower())
    check = set()
    check.add('j')  # remove J from the set
    playfair_str = []

    for char in matrix_list:
        if char in check:
            pass
        elif char not in check:
            check.add(char)
            playfair_str.append(char)

    matrix = [[0] * 5 for i in range(5)]
    counter = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = playfair_str[counter]
            counter += 1

    # for i in matrix:
    #     print(i)

    return matrix


def remove_repeat(plaintext):
    x = map(''.join, zip_longest(*[iter(plaintext)]*2, fillvalue='x'))
    y = list(x)
    p = []

    for repeat in y:
        if repeat[0] == repeat[1]:
            repeat = repeat[0] + 'x'
            p.append(repeat)
        else:
            p.append(repeat)
    # print(p)

    return p


def encrypt(keyword, plaintext):
    m = create_matrix(keyword)
    p = remove_repeat(plaintext)


# 0,1 3,4

# 0,4 3,1

keyword = input('Enter Keyword: ')
plaintext = 'ddaviidst'
encrypt(keyword, plaintext)
