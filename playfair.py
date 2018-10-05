from itertools import zip_longest

def display_matrix(matrix):
    for i in matrix:
        print(i)
    print('\n')


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

    display_matrix(matrix)

    return matrix


def remove_repeat(plaintext):
    x = map(''.join, zip_longest(
        *[iter(plaintext.replace(' ', ""))]*2, fillvalue='x'))
    y = list(x)
    p = []

    for repeat in y:
        if repeat[0] == repeat[1]:
            repeat = repeat[0] + 'x'
            p.append(repeat)
        else:
            p.append(repeat)
    # print('\n', p)  # prints plaintext grouped into pairs

    return p


def search_matrix(matrix, p):
    index = []

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == p:
                index.append(i)
                index.append(j)
    return index


def encrypt(keyword, plaintext):
    m = create_matrix(keyword)
    p = remove_repeat(plaintext)
    ciphertext = []

    for pair in p:
        x = pair[0]  # [str][str]
        y = pair[1]
        index_x = search_matrix(m, x)
        index_y = search_matrix(m, y)

        # If both characters in same row
        if index_x[0] == index_y[0]:
            if index_x[1] == 4:     # if at end of row, will go to start of row
                index_x[1] = 0
                index_y[1] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            elif index_y[1] == 4:     # if at end of row, will go to start of row
                index_y[1] = 0
                index_x[1] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            else:
                index_x[1] += 1
                index_y[1] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

        # If both characters in same column
        if index_x[1] == index_y[1]:
            if index_x[0] == 4:
                index_x[0] = 0
                index_y[0] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            elif index_y[0] == 4:
                index_y[0] = 0
                index_x[0] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            else:
                index_x[0] += 1
                index_y[0] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

        # Not in same row or column
        if index_x[0] != index_y[0] and index_x[1] != index_y[1]:
            temp = index_x[1]
            index_x[1] = index_y[1]
            index_y[1] = temp

            ciphertext.append(m[index_x[0]][index_x[1]])
            ciphertext.append(m[index_y[0]][index_y[1]])

    result = "".join(ciphertext)
    return result


# 0,1   3,4
# 0,4   3,1



keyword = ('lnfzoudtgwekarimbqpcyvhxs')
plaintext = 'help is on the way'
c = encrypt(keyword, plaintext)
print(c)
