"""
print n lines
diamond
"""
n = int(input("줄 수를 입력하세요. : ")) # number of lines
"""
아래 부분에 n 개 줄의
다이아몬드 모양을
print 하는 코드를 작성하세요.
"""
# code 시작

for i in range(n//2): # header
    print((" "*((n-2*i-1)//2)) + ("*"*(2*i+1)))

if n%2:
    print("*"*n) # center line

for i in range(n//2): # footer
    i = n//2 -1 -i
    print((" "*((n-2*i-1)//2)) + ("*"*(2*i+1)))

# code 끝

print()

# 문자열을 이용하는 방법
header, footer = '', ''
stars = ''
for i in range(n//2): # header
    header = header + ((" "*((n-2*i-1)//2)) + ("*"*(2*i+1))) + '\n'
    footer = ((" "*((n-2*i-1)//2)) + ("*"*(2*i+1))) + '\n' + footer

if n%2:
    stars = header + '*'*n + '\n' + footer
else:
    stars = header + footer
print(stars)


# list 이용하는 방법
starslist = list(range(n))
for i in range(n//2):
    starslist[i] = ((" "*((n-2*i-1)//2)) + ("*"*(2*i+1)))
    starslist[n-1-i] = starslist[i]

if n%2:
    starslist[n//2] = '*'*n
for st in starslist:
    print(st)

print()
# 수열을 이용하는 방법
for i in range(n):
    a = 2*i + 1 # 1 3 5 7 9
    b = 2*n - a # 9 7 5 3 1
    nStars = min(a, b)
    nBlanks = (n - nStars)//2
    print(' '*nBlanks + '*'*nStars)

