"""
print the snail
"""


def print_matrix(mtrx):
    lenn = len(str(len(mtrx) * len(mtrx[0])))
    for i in range(len(mtrx)):
        line = ''
        for j in range(len(mtrx[i])):
            line += ' '*(lenn - len(str(mtrx[i][j]))) + str(mtrx[i][j]) + ' '
        print(line)
    print()


def snail(n):
    print('snail')
    snail = list()
    for i in range(n):
        snail.append([0]*n)
    #         left    down    right     up
    direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    d, i, j = 0, 0, 0
    for m in range(1, n*n+1):
        snail[i][j] = m
        i += direc[d][0]
        j += direc[d][1]
        if (i not in range(n)) or (j not in range(n)) or (snail[i][j] != 0):
            i -= direc[d][0]
            j -= direc[d][1]
            d = (d+1) % 4
            i += direc[d][0]
            j += direc[d][1]

    return snail


def row(n):
    print('row')
    return list(list(range(i*n + 1, (i + 1)*n + 1)) for i in range(n))


def column(n):
    print('column')
    return list(list(range(i + 1, i + n*n + 1, n)) for i in range(n))


def row_zigzag(n):
    print('row zigzag')
    return list(list(range((i*n + 1)*(1 - i%2) + ((i + 1)*n)*(i%2), ((i + 1)*n + 1)*(1 - i%2) + (i*n)*(i%2), (1 - i%2) - (i%2))) for i in range(n))


def row_zigzag2(n):
    print('row zigzag 2')
    return list(list((i*n + 1 + j)*(1 - i%2) + (n*i + n - j)*(i%2) for j in range(n)) for i in range(n))


def row_zigzag3(n):
    print('row zigzag 3')
    rz = [[0]*n for i in range(n)]
    a = 1
    for i in range(n):
        for j in range(n):
            rz[i][j*(1 - i%2) + (n - 1 - j)*(i%2)] = a
            a += 1
    return rz


n = int(input("크기를 입력하세요. : "))
print_matrix(snail(n))
print_matrix(row(n))
print_matrix(column(n))
print_matrix(row_zigzag(n))
print_matrix(row_zigzag2(n))
print_matrix(row_zigzag3(n))
