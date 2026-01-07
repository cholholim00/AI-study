import sys
import os

# ===============================
# 06-1 내가 프로그램을 만들 수 있을까?
# ===============================
name = input("이름을 입력하세요: ")
print(f"{name}님, 프로그램 만들기에 오신 걸 환영합니다!")


# ===============================
# 06-2 3과 5의 배수를 모두 더하기
# ===============================
total = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


# ===============================
# 06-3 게시판 페이징하기
# ===============================
def get_total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))


# ===============================
# 06-4 간단한 메모장 만들기 (memo.py)
# ===============================
if len(sys.argv) > 1:
    option = sys.argv[1]

    if option == '-a':
        memo = sys.argv[2]
        with open('memo.txt', 'a', encoding='utf-8') as f:
            f.write(memo + '\n')

    elif option == '-v':
        with open('memo.txt', 'r', encoding='utf-8') as f:
            print(f.read())


# ===============================
# 06-5 탭 문자를 공백 문자 4개로 바꾸기 (tab_to_space.py)
# ===============================

src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\t', ' ' * 4)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)


# ===============================
# 06-6 하위 디렉터리 검색하기
# ===============================

def search(dirname):
    for filename in os.listdir(dirname):
        full_path = os.path.join(dirname, filename)
        if os.path.isdir(full_path):
            search(full_path)
        else:
            print(full_path)

search("C:/test")
