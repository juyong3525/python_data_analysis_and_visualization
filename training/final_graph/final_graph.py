import pandas as pd
from pandas.core.accessor import register_dataframe_accessor
from pandas.core.dtypes.missing import isnull

# 최종 전처리 데이터로 그래프 만들기 part.1
# csv 파일 불러오기
df_confirmed = pd.read_csv("../../classData/COVID-19-master/final_df.csv")
# print(df_confirmed.head())
# print(df_confirmed.shape)


# 국가명과 iso2 매칭 테이블 읽기 (country_info)
country_info = pd.read_csv("../../classData/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv",
                           encoding='utf-8-sig', keep_default_na=False, na_values='')
# print(country_info.head())
# print(country_info[country_info['Country_Region'] == 'Namibia'])
country_info = country_info[['iso2', 'Country_Region']]
# print(country_info.head())


# 중복 행 제거
# print(country_info.shape)
country_info = country_info.drop_duplicates(
    subset='Country_Region', keep='last')
# print(country_info.shape)


# 날짜별 국가별 확진자수와 국가별 iso2 값 병합
doc_final_country = pd.merge(
    df_confirmed, country_info, how='left', on='Country_Region')
# print(doc_final_country.head())
# print(doc_final_country.shape)


# 없는 데이터 확인하기
# print(doc_final_country.isnull().sum())
# print(doc_final_country[doc_final_country['iso2'].isnull()])
doc_final_country = doc_final_country.dropna(subset=['iso2'])
# print(doc_final_country[doc_final_country['iso2'].isnull()])
# print(doc_final_country.head())


# 국기 링크를 기존 컬럼 기반해서 만들어, 데이터프레임에 붙이기
def create_flag_link(row):
    flag_link = 'https://www.countryflags.io/' + row + '/flat/64.png'
    return flag_link


doc_final_country['iso2'] = doc_final_country['iso2'].apply(create_flag_link)
# print(doc_final_country.head())


# 데이터프레임 컬럼 조정하기
cols = doc_final_country.columns.tolist()
cols.remove('iso2')
cols.insert(1, 'iso2')
doc_final_country = doc_final_country[cols]
# print(doc_final_country.head())


# 컬럼명 변경
cols[1] = 'Country_Flag'
doc_final_country.columns = cols
# print(doc_final_country.head())


# 최공 가공 완료 파일 저장
doc_final_country.to_csv(
    "../../classData/COVID-19-master/final_covid_data_for_graph.csv")
