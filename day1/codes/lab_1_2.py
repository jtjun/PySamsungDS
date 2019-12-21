today = int(input("오늘은 무슨 요일입니까? (월: 1 ~ 일: 7): "))
duration = int(input("며칠 뒤의 요일을 알고 싶습니까?: "))

future = (today + duration - 1) % 7 + 1
print("그 날의 요일은 " + str(future) + "입니다. (월: 1 ~ 일: 7)")
