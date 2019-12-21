count = 0

answer = int(input("71 + 42 = "))
count = count + int(answer == 71 + 42)

answer = int(input("153 + 188 = "))
count = count + int(answer == 153 + 188)

answer = int(input("321 + 1016 = "))
count = count + int(answer == 321 + 1016)

print("3개 중 " + str(count) + "개 맞았습니다.")
