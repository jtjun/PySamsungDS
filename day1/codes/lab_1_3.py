number = float(input("반올림할 수를 입력해 주세요: "))
rounded = int(number + ((number % 1) // 0.5))

print("반올림 결과는 " + str(rounded) + "입니다.")
