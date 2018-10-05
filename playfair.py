# David Maldonado
# Cryptography

from itertools import zip_longest
import fileinput


def read_file(filename):
    plain_cipher = ""
    for line in fileinput.input(filename):
        # \n will count as a character if not removed
        plain_cipher += line.replace('\n', '')
    return plain_cipher


def write_plaintext(text):
    output = open('out2.txt', 'w')
    output.write(text)
    output.close()


def write_ciphertext(text):
    output = open('out1.txt', 'w')
    output.write(text)
    output.close()


def display_matrix(matrix):
    for i in matrix:
        print(i)
    print()


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
                index_x[0] = 0      # if at bottom of col, will go to top
                index_y[0] += 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            elif index_y[0] == 4:
                index_y[0] = 0      # if at bottom of col, will go to top
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


def decrypt(keyword, plaintext):
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
            if index_x[1] == 0:     # if at start of row, will go to end of row
                index_x[1] = 4
                index_y[1] -= 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            elif index_y[1] == 0:     # if at start of row, will go to end of row
                index_y[1] = 4
                index_x[1] -= 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            else:
                index_x[1] -= 1
                index_y[1] -= 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

        # If both characters in same column
        if index_x[1] == index_y[1]:
            if index_x[0] == 0:     # if at top of col, will go to bottom
                index_x[0] = 4
                index_y[0] -= 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            elif index_y[0] == 0:
                index_y[0] = 4      # if at top of col, will go to bottom
                index_x[0] -= 1

                ciphertext.append(m[index_x[0]][index_x[1]])
                ciphertext.append(m[index_y[0]][index_y[1]])

            else:
                index_x[0] -= 1
                index_y[0] -= 1

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

# Homework keyword for checking
# lnfzoudtgwekarimbqpcyvhxs
# help is on the way

print('Have content in your Plaintext.txt and Ciphertext.txt files!')
choice = ""
while True:
    choice = input('Choose an option.\n1. Encrypt\n2. Decrpt\n')
    if choice == '1' or choice == '2':
        break


if choice == '1':
    keyword = input('Enter your keyword. ')
    plaintext = read_file('Plaintext.txt')
    ciphertext = encrypt(keyword, plaintext)
    write_ciphertext(ciphertext)
    print('Check out1.txt for your ciphertext')

if choice == '2':
    keyword = input('Enter your keyword. ')
    ciphertext = read_file('Ciphertext.txt')
    plaintext = decrypt(keyword, ciphertext)
    write_plaintext(plaintext)
    print('Check out2.txt for your Plaintext')