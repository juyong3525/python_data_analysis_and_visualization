# pandas 라이브러리로 실제 데이터 전처리하기 part.1
# raw data 가져오기
import pandas as pd
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
