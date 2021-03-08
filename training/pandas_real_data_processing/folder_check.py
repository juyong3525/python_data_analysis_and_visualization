# pandas 라이브러리로 실제 데이터 전처리하기 part.4
# 참고: 특정 폴더 파일 리스트 확인하기
import os

PATH = "../../classData/COVID-19-master/csse_covid_19_data/all_csse_covid_19_daily_reports/"
file_list = os.listdir(PATH)
csv_list = list()
csv_list_2020 = list()
csv_list_2021 = list()

for file in file_list:
    if file.split('.')[-1] == 'csv':
        csv_list.append(file)

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

for item in csv_list:
    print(item)
