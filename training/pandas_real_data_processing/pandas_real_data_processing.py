# pandas 라이브러리로 실제 데이터 전처리하기 part.1
# raw data 가져오기
import pandas as pd
import json
PATH = "../../classData/COVID-19-master/csse_covid_19_data/all_csse_covid_19_daily_reports/"
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')

try:
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]
except:
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']
# print(doc.head())


# 데이터프레임 데이터 변환하기
doc = doc.dropna(subset=['Confirmed'])
doc = doc.astype({'Confirmed': 'int64'})
# print(doc.head())
# print(doc.groupby('Country_Region').sum())


# 국가 정보 가져오기
country_info = pd.read_csv(
    "../../classData/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')


# 두 데이터 프레임 합쳐보기
test_df = pd.merge(doc, country_info, how='left', on='Country_Region')
# print(test_df.info())
# print(test_df.isnull().sum())
nan_rows = test_df[test_df['iso2'].isnull()]
nan_rows = nan_rows[['Province_State_x', 'Country_Region', 'iso2']]
# print(nan_rows.head())


# pandas 라이브러리로 실제 데이터 전처리하기 part.2
# 컬럼 값 변경하기
def func(row):
    if row['Country_Region'] in json_data:
        row['Country_Region'] = json_data[row['Country_Region']]
    return row


with open('../../classData/COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    # print(json_data.keys())
    doc = doc.apply(func, axis=1)
    # print(doc.head())


# pandas 라이브러리로 실제 데이터 전처리하기 part.3
# 참고. 파일명으로 데이터 변환하기
data = '01-22-2020.csv'
date_column = data.split('.')[0].lstrip('0').replace('-', '/')
doc.columns = ['Province_State', 'Country_Region', date_column]
# print(doc.head())


# 중복 데이터 합치기
doc = doc.groupby('Country_Region').sum()
print(doc)
