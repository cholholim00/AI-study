# 요구 사항 정리
# Alice의 카드 N개의 공격력 A1, A2, ..., AN과 Bob의 카드 N개의 점수 B1, B2, ..., BN이 주어집니다.
# 다음과 같은 계산법을 모든 i에 대헤 적용합니다.


# 알고리즘 정리
# 모든 i에 대해 계산법을 적용해서 두 사람의 점수를 구하는 구현 문제입니다.
# 시간 복잡도는 O(N)입니다.

N = int(input()) # 각자의 카드 장수
A = list(map(int, input().split())) # 앨리스의 카드 공격력 리스트
B = list(map(int, input().split())) # 밥의 카드 공격력 리스트

# 게임 시작전에 점수 변수 0으로 초기화
alice = 0
bob = 0

for i in range(N): # i = 0 ~ N-1 (같은 인덱스 카드끼리 비교)
    if A[i] == B[i]: # -1 카드가 같은 경우 (공격력이 같으면 둘 다 1점)
        alice += 1
        bob += 1
    else: # -2 카드가 다른 경우
        diff = abs(A[i] - B[i]) # diff - 공격력 차이, abs() - 절대값
        if diff >= 7: # 차이가 7일때 (특별 규칙이다.)
            if A[i] > B[i]: # 큰쪽 / 작은쪽 구분
                alice += 1
                bob += 3
            else:
                bob += 1
                alice += 3
        else: # 차이가 7미만일 때 (기본 규칙)
            if A[i] > B[i]:
                alice += 2
            else:
                bob += 2

print(alice, bob) # 모든 카드 비교후 누락된 점수 출력