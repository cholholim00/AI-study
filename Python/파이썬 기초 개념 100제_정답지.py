# 🟢 Part 1. 출력과 변수 (001~010)
# 001. Hello World 출력
print("Hello World")

# 002. 두 줄 출력 (방법1)
print("Hello")
print("World")

# 003. 줄바꿈 문자 사용 (\n)
print("Hello\nWorld")

# 004. 작은따옴표 출력 (큰따옴표로 감싸기)
print("'Hello'")

# 005. 큰따옴표 출력 (작은따옴표로 감싸기)
print('"Hello"')

# 006. 특수문자 출력
print("!@#$%^&*()")

# 007. 파일 경로 (백슬래시는 두 번 써야 함)
print("C:\\Windows\\System32")

# 008. 정수형 변수
a = 10
print(a)

# 009. 문자열 변수
b = "Python"
print(b)

# 010. 변수 동시 출력
a = 10
b = 20
print(a, b)

# 🟡 Part 2. 입력과 자료형 (011~020)
# 011. 문자 1개 입력
data = input()
print(data)

# 012. 정수 1개 입력 (int 변환 필수)
n = int(input())
print(n)

# 013. 실수 1개 입력
f = float(input())
print(f)

# 014. 정수 2개 줄 바꿔 입력
a = int(input())
b = int(input())
print(a)
print(b)

# 015. 단어 2개 순서 바꿔 출력
w1 = input()
w2 = input()
print(w2, w1)

# 016. 문자열 반복
f = float(input())
print(f)
print(f)
print(f)
# 또는 for문 사용: for _ in range(3): print(f)

# 017. 시간 출력
time = input() # 12:30 입력 가정
print(time)

# 018. 연월일 형식 (f-string 사용 추천)
y = input()
m = input()
d = input()
print(f"{y}.{m}.{d}")

# 019. 주민번호 뒷자리 가리기 (슬라이싱)
s = input() # 900101-1234567
print(s[:7] + "*******")

# 020. 한 글자씩 나누어 출력
word = input()
for char in word:
    print(char)

# 🟠 Part 3. 연산자 (021~035)
# 021. 합계
a, b = map(int, input().split())
print(a + b)

# 022. 뺄셈
a, b = map(int, input().split())
print(a - b)

# 023. 곱셈
a, b = map(float, input().split())
print(a * b)

# 024. 문장 반복
w = input()
n = int(input())
print(w * n)

# 025. 거듭제곱
a, b = map(int, input().split())
print(a ** b)

# 026. 나눗셈 (실수 결과)
a, b = map(float, input().split())
print(a / b)

# 027. 몫 구하기
a, b = map(int, input().split())
print(a // b)

# 028. 나머지 구하기
a, b = map(int, input().split())
print(a % b)

# 029. 반올림 (소수 둘째 자리)
f = float(input())
print(round(f, 2))
# 또는 print(f"{f:.2f}")

# 030. 비트 시프트
n = int(input())
print(n << 1) # 2배
print(n >> 1) # 1/2배

# 031. 작다 (<) 비교
a, b = map(int, input().split())
print(a < b)

# 032. 같다 (==) 비교
a, b = map(int, input().split())
print(a == b)

# 033. 다르다 (!=) 비교
a, b = map(int, input().split())
print(a != b)

# 034. 논리연산 AND (둘 다 참일 때)
a, b = map(int, input().split())
print(bool(a) and bool(b))
# 또는 print(a != 0 and b != 0)

# 035. 논리연산 OR (하나라도 참일 때)
a, b = map(int, input().split())
print(bool(a) or bool(b))

# 🔵 Part 4. 조건문 (036~050)
# 036. 10보다 작은지 판별
n = int(input())
if n < 10:
    print("small")

# 037. 0이 아닐 때 출력
n = int(input())
if n != 0:
    print(n)

# 038. 더 큰 수 출력
a, b = map(int, input().split())
if a > b: print(a)
else: print(b)

# 039. 가장 작은 수 (min 함수 없이)
a, b, c = map(int, input().split())
m = a
if b < m: m = b
if c < m: m = c
print(m)

# 040. 짝수 홀수
n = int(input())
if n % 2 == 0: print("even")
else: print("odd")

# 041. 양수 음수 0
n = int(input())
if n > 0: print("plus")
elif n < 0: print("minus")
else: print("zero")

# 042. 학점 계산
s = int(input())
if s >= 90: print("A")
elif s >= 80: print("B")
elif s >= 70: print("C")
elif s >= 60: print("D")
else: print("F")

# 043. 계절 판별
m = int(input())
if 3 <= m <= 5: print("봄")
elif 6 <= m <= 8: print("여름")
elif 9 <= m <= 11: print("가을")
else: print("겨울")

# 044. 주사위 상금 (예시 로직)
dice = int(input())
if dice == 1: print("1등")
elif dice == 2: print("2등")
else: print("꽝")

# 045. 윤년 판별
y = int(input())
if (y%4==0 and y%100!=0) or (y%400==0):
    print("Yes")
else:
    print("No")

# 046. 이벤트 당첨 (홀수 번째 방문자 당첨 가정)
n = int(input())
if n % 2 != 0: print("이벤트 당첨")
else: print("다음 기회에")

# 047. 로그인
uid = input(); upw = input()
if uid == "admin" and upw == "1234":
    print("Login Success")
else:
    print("Login Fail")

# 048. 사칙연산 계산기
a = int(input())
op = input()
b = int(input())
if op == '+': print(a+b)
elif op == '-': print(a-b)
elif op == '*': print(a*b)
elif op == '/': print(a/b)

# 049. 큰 수 - 작은 수
a, b = map(int, input().split())
if a > b: print(a - b)
else: print(b - a)

# 050. BMI 계산
h = float(input()) # 키(m)
w = float(input()) # 몸무게(kg)
bmi = w / (h**2)
if bmi >= 25: print("비만")
else: print("정상")

# 🟣 Part 5. 반복문 (051~070)
# 051. 1~100 출력
for i in range(1, 101):
    print(i)

# 052. 1~n 출력
n = int(input())
for i in range(1, n+1):
    print(i)

# 053. 카운트다운
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 054. 알파벳 순서 출력
c = input() # 'f' 입력 가정
start = ord('a')
end = ord(c)
for i in range(start, end+1):
    print(chr(i), end=' ')

# 055. 1~100 짝수만
for i in range(1, 101):
    if i % 2 == 0: print(i)

# 056. 1~n 합계
n = int(input()); s = 0
for i in range(1, n+1): s += i
print(s)

# 057. 3의 배수의 합
n = int(input()); s = 0
for i in range(1, n+1):
    if i % 3 == 0: s += i
print(s)

# 058. 0 입력까지 더하기
s = 0
while True:
    n = int(input())
    if n == 0: break
    s += n
print(s)

# 059. 합이 100 넘을 때 종료
s = 0; i = 0
while s <= 100:
    i += 1
    s += i
print(i) # 그때의 숫자

# 060. 3의 배수 건너뛰기
n = int(input())
for i in range(1, n+1):
    if i % 3 == 0: continue
    print(i, end=' ')

# 061. 구구단 2단
for i in range(1, 10):
    print(f"2 * {i} = {2*i}")

# 062. 구구단 전체
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")

# 063. 정사각형 별
n = int(input())
for i in range(n):
    print("*" * n)

# 064. 직각삼각형 (왼쪽)
n = int(input())
for i in range(1, n+1):
    print("*" * i)

# 065. 직각삼각형 (오른쪽)
n = int(input())
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)

# 066. 피라미드
n = int(input())
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# 067. 역삼각형
n = int(input())
for i in range(n, 0, -1):
    print("*" * i)

# 068. 타이머
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # 1초 대기

# 069. 주사위 합 10
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 10:
            print(i, j)

# 070. 팩토리얼
n = int(input()); fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 🟤 Part 6. 리스트 (071~085)
# 071. 추가
a = []
a.append(1); a.append(2); a.append(3)
print(a)

# 072. 인덱싱
a = [10, 20, 30]
print(a[1])

# 073. 합계
a = [10, 20, 30]
print(sum(a))

# 074. 최대최소
a = [5, 2, 8, 1]
print(max(a), min(a))

# 075. 뒤집기
a = [1, 2, 3]
print(a[::-1])

# 076. 정렬
a = [3, 1, 2]
a.sort()
print(a)

# 077. 삭제
a = [10, 20, 30]
a.remove(20) # 값으로 삭제
# 또는 del a[1] (인덱스로 삭제)
print(a)

# 078. 삽입
a = [10, 30]
a.insert(1, 20) # 1번 인덱스에 20 삽입
print(a)

# 079. 존재 확인
names = ["Kim", "Lee", "Park"]
if "Kim" in names: print("있음")

# 080. 문자열 분리
s = "Hello Python"
arr = s.split()
print(arr)

# 081. 문자열 합치기
arr = ["Hello", "Python"]
s = " ".join(arr)
print(s)

# 082. 2차원 리스트
m = [[1, 2], [3, 4]]
print(m[0][0], m[1][1])

# 083. 바둑판 (간단 예시)
board = [[0]*19 for _ in range(19)]
x, y = map(int, input().split())
board[x][y] = 1 # 흰돌
print("놓기 완료")

# 084. 홀수만 저장
nums = []
for _ in range(10):
    n = int(input())
    if n % 2 != 0: nums.append(n)
print(nums)

# 085. 로또
import random
lotto = random.sample(range(1, 46), 6)
lotto.sort()
print(lotto)

# ⚫ Part 7. 응용과 함수 (086~100)
# 086. 딕셔너리 기초
d = {'apple':'사과', 'banana':'바나나'}
print(d['apple'])

# 087. 단어장
d = {}
while True:
    w = input()
    if w == 'q': break
    if w in d: print(d[w])
    else: d[w] = input("뜻?")

# 088. 키 출력
d = {'a':1, 'b':2}
print(list(d.keys()))

# 089. 값 출력
print(list(d.values()))

# 090. 빈도수 세기
s = "banana"
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1
print(count)

# 091. 함수 정의
def say_hello():
    print("Hello")
say_hello()

# 092. 합 함수
def add(a, b):
    return a + b
print(add(3, 5))

# 093. 짝수 판별 함수
def is_even(n):
    return n % 2 == 0
print(is_even(4))

# 094. 평균 함수
def get_avg(lst):
    return sum(lst) / len(lst)
print(get_avg([80, 90, 100]))

# 095. 거스름돈
def change(money):
    coins = [500, 100, 50, 10]
    for coin in coins:
        cnt = money // coin
        print(f"{coin}원: {cnt}개")
        money %= coin
change(1260)

# 096. 소수 판별
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print(is_prime(17))

# 097. 재귀 합
def recursive_sum(n):
    if n == 1: return 1
    return n + recursive_sum(n-1)
print(recursive_sum(10))

# 098. 파일 쓰기
f = open("test.txt", "w")
f.write("Hello Python")
f.close()

# 099. 파일 읽기
f = open("test.txt", "r")
print(f.read())
f.close()

# 100. 업다운 게임
import random
ans = random.randint(1, 100)
while True:
    n = int(input())
    if n > ans: print("Down")
    elif n < ans: print("Up")
    else:
        print("Correct!")
        break








