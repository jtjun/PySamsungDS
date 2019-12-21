korean = int(input("국어 점수: "))
math = int(input("수학 점수: "))
english = int(input("영어 점수: "))

length = (korean + 5) // 10
print('국어 ' + '#' * length + ' ' * (10 - length) + ' ' + str(korean))

length = (math + 5) // 10
print('수학 ' + '#' * length + ' ' * (10 - length) + ' ' + str(math))

length = (english + 5) // 10
print('영어 ' + '#' * length + ' ' * (10 - length) + ' ' + str(english))