P = float(input("원금을 입력하세요: "))
r = float(input("연이율을 입력하세요 (% 단위, 숫자만 입력): "))
n = int(input("만기까지의 기간을 입력하세요 (년): "))

A = (1 + r / 100) ** n * P

print("만기 금액은 " + str(A) + "입니다.")
