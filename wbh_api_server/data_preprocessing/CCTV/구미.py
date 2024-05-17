import sqlite3
import pandas as pd

# 엑셀 파일 경로
excel_file_path = "Z:/WayBackHome/DataSet/구미CCTV정보.xlsx"

# SQLite 데이터베이스 경로
db_path = "Z:/WayBackHome/BackendServer/wbh_api_server/db.sqlite3"

# 엑셀 파일에서 데이터를 읽어옵니다.
data = pd.read_excel(excel_file_path)

# 데이터베이스 연결을 엽니다.
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 데이터 삽입 쿼리
insert_query = """
INSERT INTO data_api_cctv (
    area_code,
    number,
    managing_agency,
    address_road,
    address_jibun,
    purpose,
    camera_count,
    resolution,
    direction_info,
    retention_period,
    installation_date,
    managing_agency_phone,
    latitude,
    longitude,
    data_standard_date
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# 데이터를 순회하면서 데이터베이스에 삽입합니다.
for index, row in data.iterrows():
    print(f"{index}행 삽입")
    cursor.execute(insert_query, (
        "구미",  # 행정지역명
        row['번호'],
        row['관리기관명'],
        row['소재지도로명주소'],
        row['소재지지번주소'],
        row['설치목적구분'],
        row['카메라대수'],
        row['카메라화소수'],
        row['촬영방면정보'],
        row['보관일수'],
        row['설치연월'],
        row['관리기관전화번호'],
        row['WGS84위도'],
        row['WGS84경도'],
        row['데이터기준일자']
    ))

# 변경사항 저장
conn.commit()

# 데이터베이스 연결을 닫습니다.
conn.close()

print("Data 삽입 완료.")