%matplotlib inline
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime 
import pandas as pd #판다스 library 불러오기
import numpy as np

df = pd.read_csv("SUBWAY.csv",encoding='utf-8',parse_dates=['STD_DATE']) #공공데이터파일 불러오기

df['Year']=df['STD_DATE'].dt.year #Year에 STD_DATE를 연도별로 분류한 데이터 저장
DATE_YEAR=df.groupby('Year')['ALL_AVG_USER'].aggregate(['max','min','mean']).reset_index() #Year 별로 ALL_AVG_USER에 대한 최대,최소,평균
DATE_YEAR

#seaborn을 이용한 막대그래프
plt.rcParams['figure.figsize'] =[15,5]
sns.barplot(
    data =DATE_YEAR,
    x = "Year",
    y = "mean"
)
plt.title("연평균 전국 지하철 이용객 평균")
plt.show()

#최근 5년간의 이용객 평균을 곡선그래프로 나타내기
ALL_DATE = df.groupby('STD_DATE').mean().assign(counts=df['STD_DATE'].value_counts()) #날짜별 평균이용객 집계

Recent_DATE=DATE.tail(60)
Recent_DATE['ALL_AVG_USER'].plot(figsize=(12,4)) #ALL_AVG_USER의 데이터를 그래프로 그림

#월별 이용객 최대, 최소, 평균
df['Month']=df['STD_DATE'].dt.month
DATE_Month=df.groupby('Month')['ALL_AVG_USER'].aggregate(['max','min','mean']).reset_index()
DATE_Month
 
#지정한 년도의 데이터만 보여줌
target_year = '2020'
DATE=df.query('STD_DATE.dt.year == @target_year')
DATE.groupby('STD_DATE').mean().assign(counts=df['STD_DATE'].value_counts())

AREA=df.groupby('SUBW_AREA_NM')['ALL_AVG_USER'].aggregate(['sum','max','min','mean']).reset_index()
AREA_AVG=AREA['mean']
AREA_AVG.index=['광주','대구','대전','부산','수도권']

AREA_AVG.plot.pie(figsize=(7,7),autopct='%1.1f%%',startangle=30,shadow=True, textprops={'size':15})
plt.title('지역별 지하철 평균 탑승객',size =20)

plt.legend(AREA_AVG.index=='SUBW_AREA_NM')
plt.show()
 
