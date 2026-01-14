import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- 설정 ---
TARGET_URL = "https://product.kyobobook.co.kr/bestseller/total?saleCmdtDvsnCode=TOT&dsplDvsnCode=001"
FILE_NAME = "kyobo_links.csv"
# -----------

print("🚀 교보문고 [링크 추적] 로봇 가동!")

options = Options()
# 로봇 감지 회피
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    print(f"🌐 접속 중... {TARGET_URL}")
    driver.get(TARGET_URL)

    print("⏳ 데이터 로딩 대기 (7초)...")
    time.sleep(7)

    # 스크롤을 내려서 아래쪽 책들도 깨웁니다.
    print("📜 스크롤 다운...")
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(3)

    print("🔎 '상세 페이지'로 연결되는 모든 링크를 수집합니다...")

    # [핵심 전략]
    # 태그나 클래스 이름 무시!
    # href 속성에 '/detail/' 이라는 글자가 포함된 모든 a태그(링크)를 찾습니다.
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/detail/']")

    print(f"🎯 발견된 링크 개수: {len(links)}개 (이미지 링크 포함)")

    book_data = []
    seen_titles = set() # 중복 제거용 (이미지와 제목이 같은 링크를 쓰므로)

    for link in links:
        try:
            # 링크 안에 있는 텍스트(책 제목)를 가져옵니다.
            title = link.text.strip()
            href = link.get_attribute("href")

            # 1. 제목이 비어있지 않고 (이미지 링크 제외)
            # 2. 제목 길이가 2글자 이상이며
            # 3. 이미 수집한 제목이 아닐 때만 저장
            if title and len(title) > 2 and title not in seen_titles:
                # 불필요한 텍스트(장바구니 담기 등) 걸러내기
                if "장바구니" in title or "바로가기" in title:
                    continue

                seen_titles.add(title)
                # 순위는 수집 순서대로 매깁니다.
                rank = len(seen_titles)

                print(f"{rank}위 | {title[:20]}...")
                book_data.append([rank, title, href])

                if len(book_data) >= 20: # 20개 찾으면 퇴근
                    break
        except:
            continue

    if len(book_data) > 0:
        with open(FILE_NAME, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["순위", "제목", "링크주소"])
            writer.writerows(book_data)
        print(f"\n🎉 대성공! '{FILE_NAME}' 파일에 저장했습니다.")
    else:
        print("\n❌ 0개입니다.")
        print("이건 정말 이상하네요. 브라우저 화면에 책이 보이긴 하나요?")

except Exception as e:
    print(f"⚠️ 에러 발생: {e}")

finally:
    print("작업 종료.")
    driver.quit()