# 요구 사항 정리
# Alice의 카드 N개의 공격력 A1, A2, ..., AN과 Bob의 카드 N개의 점수 B1, B2, ..., BN이 주어집니다.
# 다음과 같은 계산법을 모든 i에 대헤 적용합니다.


# 알고리즘 정리
# 모든 i에 대해 계산법을 적용해서 두 사람의 점수를 구하는 구현 문제입니다.
# 시간 복잡도는 O(N)입니다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

alice = 0
bob = 0
for i in range(N):
    if A[i] == B[i]: # Draw
        alice += 1
        bob += 1
    elif A[i] > B[i]: # Alice > Bob
        if A[i] - B[i] == 7: # dif is 7
            alice -= 1
            bob += 3
        else:
            alice += 2
    else: # Bob > Alice
        if B[i] - A[i] == 7: # dif is 7
            alice += 3
            bob -= 1
        else:
            bob += 2

print(alice, bob)