print("========== 클래스 ==========")
print("[계산기의 ‘더하기’ 기능 : 1대]")
result = 0
def add(num):
    global result # result 전역 변수(global): 이전에 계산한 결괏값을 유지
    result = result + num # 결과값에 입력값 더하기
    return result
print(add(5))
print(add(10))
print("[계산기의 ‘더하기’ 기능 : 2대]")
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 = result1 + num
    return result1
def add2(num):
    global result2
    result2 = result2 + num
    return result2
print(add1(5))
print(add1(14))
print(add2(10))
print(add2(20))

print("[클래스를 사용]")
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(5))
print(cal1.add(10))
print(cal2.add(15))
print(cal2.add(20))

print("[클래스 구조 만들기 : 만들기중....]")
class FourCal:
    def __init__(self): # 생성자
        self.num1 = 0
        self.num2 = 0

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self): # 더하기 기능 만들기 메서드
        return self.num1 + self.num2

    def sub(self): # 빼기 기능 만들기 메서드
        return self.num1 - self.num2

    def mul(self): # 곱하기 기능 만들기 메서드
        return self.num1 * self.num2

    def div(self): # 나누기 기능 만들기 메서드
        return self.num1 / self.num2

print("[사칙 연산 클래스 만들기]")
a = FourCal()
a.setdata(10, 20)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print("[클래스의 상속]")
class MoreFourCal(FourCal):
    def pow(self): # 거듭제곱 기능 추가 만들기 메서드
        return self.num1 ** self.num2
a = MoreFourCal()
print(a.pow())

print("========== 모듈 ==========")
print("========== 패키지 ==========")
print("========== 예외처리 ==========")
print("========== 내장 함수 ==========")
print("========== 표준 라이브러리 ==========")
print("========== 외부 라이브러리 ==========")
