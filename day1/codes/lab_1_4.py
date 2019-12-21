hour = float(input("시침 값을 입력해주세요: "))
minute = float(input("분침 값을 입력해주세요: "))

hour_angle = hour * (360 / 12)
minute_angle = minute * (360 / 60)

hour_angle = hour_angle + minute / 60 * (360 / 12)

angle = (minute_angle - hour_angle) % 360
print("시침에 대한 분침의 각도는 " + str(angle) + "도입니다.")
