# # CH04 (데이터 수술하기 (추출과 정렬))
import pandas as pd

medical_data = pd.read_csv('patient_data.csv')
print("--- 원본 데이터 ---")
print(medical_data)

# **No.11 조건 필터링:** "30대 여성이면서 혈압이 130 이상인 사람 뽑기" (`&`(그리고), `|`(또는) 연산자)
filter_df = (medical_data["나이"] >= 30) & (medical_data["나이"] < 40) & (medical_data["혈압"]>= 130)
df = medical_data[filter_df]
print("\n--- 1. 필터링 결과 (30대 & 혈압 130↑) ---")
print(df)

# **No.12 정렬하기 (`sort_values`):** "혈당 높은 순서대로 줄 세우기"
sort_df = medical_data.sort_values(by='혈당', ascending=False)
print("\n--- 2. 혈당 높은 순서대로 줄 세우기 ---")
print(sort_df)

# **No.13 특정 열만 뽑기:** 전체 데이터에서 '이름'과 '진단명'만 남기기
select_df = medical_data[["이름", "진단명"]]
print("\n--- 3. 특정 열 선택 결과 ---")
print(select_df)

# - **No.14 "고위험군 랭킹 매기기"**
# - 가상의 환자 데이터 10개를 만들고, **'나이가 60세 이상'**이면서 **'혈당이 140 이상'**인 환자를 뽑은 뒤, **혈당이 높은 순서대로** 정렬해서 출력하세요.
