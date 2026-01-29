import pandas as pd
import os

# 1. 파일 경로 설정
base_path = os.path.dirname(os.path.abspath(__file__))
file_name = '질병관리청_코로나19 확진자 발생현황(전수감시)_20230831.csv'
full_path = os.path.join(base_path, file_name)

def final_clean():
    try:
        print("🚀 모든 데이터(사망자/지역 포함) 최종 정제를 시작합니다...")
        # 실제 파일은 엑셀 구조이므로 read_excel 사용
        df = pd.read_excel(full_path, skiprows=4, engine='openpyxl')
        
        # 컬럼명 공백 제거
        df.columns = [str(col).strip() for col in df.columns]
        
        # [핵심] 컬럼명 한글 -> 영어 표준화
        # 엑셀 시트 순서에 의거하여 정확하게 이름을 붙여줍니다.
        col_names = ['date', 'total', 'domestic', 'overseas', 'death', 
                     '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', 
                     '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '검역']
        
        # 현재 df의 컬럼 수에 맞춰 이름을 할당 (데이터 부족 시 방지)
        df.columns = col_names[:len(df.columns)]
        
        # 2. 데이터 세척 (2020년 이후 데이터만)
        df = df[df['date'].astype(str).str.contains('20', na=False)].copy()
        
        # 모든 숫자 컬럼 쉼표 제거 및 정수형 변환
        for col in df.columns:
            if col != 'date':
                df[col] = df[col].astype(str).str.replace(',', '').str.replace(' ', '')
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        
        # 날짜 형식 최종 변환 및 정렬
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date').reset_index(drop=True)
        
        # 3. 결과 저장 (data 폴더 생성 후 저장)
        output_dir = os.path.join(base_path, 'data')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'cleaned_covid_data.csv')
        
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"\n✅ [대성공] 모든 팀원이 즉시 사용 가능한 파일이 생성되었습니다!")
        print(f"📊 저장 위치: {output_path}")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    final_clean()