# 전처리 : geocode - 구글 스프레드시트에 awesome map을 사용

import sqlite3
import pandas as pd

# 엑셀 파일 경로
excel_file_path = "Z:/WayBackHome/DataSet/전국비상벨스마트가로등.xlsx"

# SQLite 데이터베이스 경로
db_path = "Z:/WayBackHome/BackendServer/wbh_api_server/db.sqlite3"

# 엑셀 파일에서 데이터를 읽어옵니다.
data = pd.read_excel(excel_file_path)

# 데이터베이스 연결을 엽니다.
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 기존 테이블이 존재하면 삭제합니다.
drop_table_query = "DROP TABLE IF EXISTS data_api_alarmbell"
cursor.execute(drop_table_query)

# 새로운 테이블을 생성합니다.
create_table_query = """
CREATE TABLE data_api_alarmbell (
    type VARCHAR(100) NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL
)
"""
cursor.execute(create_table_query)

# 데이터 삽입 쿼리
insert_query = """
INSERT INTO data_api_alarmbell (
    type,
    latitude,
    longitude
) VALUES (?, ?, ?)
"""

# 데이터를 순회하면서 데이터베이스에 삽입합니다.
for index, row in data.iterrows():
    print(f"{index}행 삽입")
    cursor.execute(insert_query, (
        row['TYPE'],
        row['LA'],
        row['LO']
    ))

# 변경사항 저장
conn.commit()

# 데이터베이스 연결을 닫습니다.
conn.close()

print("Data 삽입 완료.")
