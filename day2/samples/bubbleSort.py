"""
sort n elements
by bubble sort
"""
"""
아래 부분에
길이 n 을 먼저 input으로 받고
n 개의 숫자를 input으로 받아 
list 를 만드세요.
"""
# code 시작

n = int(input("배열 길이를 입력하세요. : "))

arr = list(range(n))
for i in range(n):
    arr[i] = int(input(str(i+1)+"번째 원소 : "))

print("정렬 전")
print(arr)

# code 끝

"""
아래 부분에 list 를
bubble sort 알고리즘으로
오름차순 정렬 후 출력하세요.
ex) [1, 2, 3, 4, 5]
"""
# code 시작

for i in range(n):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("정렬 후")
print(arr)

# code 끝
