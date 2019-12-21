"""
sort n elements
by bubble sort
"""

n = int(input("크기를 입력하세요. : "))
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

# 달팽이 배열을 n * n 형태로 출력
lenn = len(str(n*n)) # n^2 의 자리수

for i in range(n):
    line = ''
    for j in range(n):
        line += ' '*(lenn - len(str(snail[i][j]))) + str(snail[i][j]) + ' '
    print(line)
