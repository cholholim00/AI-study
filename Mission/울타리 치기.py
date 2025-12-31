

N = int(input())
A = list(map(int, input().split()))

fence = 2 * N          # 위 + 아래
fence += A[0] + A[-1]  # 왼쪽 + 오른쪽

for i in range(1, N):
    fence += abs(A[i] - A[i - 1])

print(fence)