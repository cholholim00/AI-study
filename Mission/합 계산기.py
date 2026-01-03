# 요구 사항 정리
# 주어진 문자열 형태 식을 계산하여 출력하는 문제입니다.
# 식의 부호와 수를 분리하여 연산을 수행하고, 그 결과를 모두 더하면 됩니다.

# 알고리즘 정리
# 식을 적절하게 분리하여, 더하면 됩니다.
# 시간 복잡도는 O(N)입니다.

result = 0
T = int(input())

for i in range(T):
    s = input().split()
    firstNum = int(s[0])
    command = s[1]
    secondNum = int(s[2])

    if command == "+":
        result += firstNum + secondNum
    elif command == "-":
        result += firstNum - secondNum
    elif command == "*":
        result += firstNum * secondNum
    else:
        result += firstNum // secondNum

print(result)


