# 요구 사항 정리
# 주어진 문자열 형태 식을 계산하여 출력하는 문제입니다.
# 식의 부호와 수를 분리하여 연산을 수행하고, 그 결과를 모두 더하면 됩니다.

# 알고리즘 정리
# 식을 적절하게 분리하여, 더하면 됩니다.
# 시간 복잡도는 O(N)입니다.

T = int(input())
result = 0

for _ in range(T):
    a, op, b = input().split()
    a = int(a)
    b = int(b)

    if op == '+':
        result = a + b # 덧셈 결과
    elif op == '-':
        result = a - b # 뺄셈 결과
    elif op == '*':
        result = a * b # 곱셉 결과
    elif op == '/':
        result = a // b # 정수 나눗셈 결과
print(result)


