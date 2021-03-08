import pandas as pd
import json
import os

# pandas 라이브러리로 실제 데이터 전처리하기 part.4
# 데이터 전처리하기 - 지금까지의 과정을 모두 한데 모아서, 함수로 만들기
with open('../../classData/COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)


def country_name_convert(row):
    if row['Country_Region'] in json_data:
        return json_data[row['Country_Region']]
    return row['Country_Region']


def create_dataframe(filename):
    doc = pd.read_csv(PATH + filename, encoding='utf-8-sig')    # csv 파일 읽기
    try:
        doc = doc[['Country_Region', 'Confirmed']]  # 특정 컬럼만 선택해서 dataFrame 만들기
    except:
        doc = doc[['Country/Region', 'Confirmed']]
        doc.columns = ['Country_Region', 'Confirmed']
    doc = doc.dropna(subset=['Confirmed'])  # 특정 컬럼에 없는 데이터 삭제하기
    # 'Country_Region'의 국가명을 여러 파일에 일관되게 변경
    doc['Country_Region'] = doc.apply(country_name_convert, axis=1)
    doc = doc.astype({'Confirmed': 'int64'})    # 특정 컬럼의 데이터 타입 변경하기
    # 특정 컬럼으로 중복된 데이터를 합치기 ('Country_Region'이 index로 됨)
    doc = doc.groupby('Country_Region').sum()

    date_column = filename.split('.')[0].lstrip('0').replace('-', '/')
    doc.columns = [date_column]
    return doc


# 특정 폴더 파일 리스트 확인하기
def generate_dataframe_by_path(PATH):
    file_list = os.listdir(PATH)
    csv_list = list()
    csv_list_2020 = list()
    csv_list_2021 = list()
    first_doc = True

    for file in file_list:
        if file.split('.')[-1] == 'csv':
            csv_list.append(file)

    # sort
    for file in csv_list:
        std = file.split('-')[2].split('.')[0]
        if std == '2020':
            csv_list_2020.append(file)
        else:
            csv_list_2021.append(file)
    csv_list_2020.sort()  # 정렬
    csv_list_2021.sort()
    csv_list = list()
    for file in csv_list_2020:
        csv_list.append(file)
    for file in csv_list_2021:
        csv_list.append(file)

    for file in csv_list:
        print(f"{file} processing...")
        doc = create_dataframe(file)
        if first_doc:
            final_doc, first_doc = doc, False
        else:
            final_doc = pd.merge(final_doc, doc, how='outer',
                                 left_index=True, right_index=True)

    final_doc = final_doc.fillna(0)
    return final_doc


PATH = "../../classData/COVID-19-master/csse_covid_19_data/all_csse_covid_19_daily_reports/"
doc = generate_dataframe_by_path(PATH)
doc = doc.astype('int64')
# print(doc)

# csv 파일로 저장
doc.to_csv("../../classData/COVID-19-master/final_df.csv",
           encoding='utf-8-sig')
