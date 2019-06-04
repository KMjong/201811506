import pandas as pd

data = pd.read_csv('data2.csv')  # 읽어들이기

# 1. 월별로 나누기
mon_1 = data.loc[0:6943,]  # 1월 행 불러오기
mon_2 = data.loc[6944:13215,]  # 2월 행 불러오기
mon_3 = data.loc[13216:20159,]  # 3월 행 불러오기
mon_4 = data.loc[20160:26879,]  # 4월 행 불러오기
mon_5 = data.loc[26880:33823,]  # 5월 행 불러오기
mon_6 = data.loc[33824:40543,]  # 6월 행 불러오기
mon_7 = data.loc[40544:47487,]  # 7월 행 불러오기
mon_8 = data.loc[47488:54431,]  # 8월 행 불러오기
mon_9 = data.loc[54432:61151,]  # 9월 행 불러오기
mon_10 = data.loc[61152:68095,]  # 10월 행 불러오기
mon_11 = data.loc[68096:74815,]  # 11월 행 불러오기
mon_12 = data.loc[74816:81759,]  # 12월 행 불러오기

# 2. 월별로 나눈 데이터의 평균을 시간별로 구하기
df_mon_1 = mon_1.groupby(['역명', '구분'], as_index=False).mean()     # groupby를 이용하여  시간대별 평균 구하기
df_mon_2 = mon_2.groupby(['역명', '구분'], as_index=False).mean()
df_mon_3 = mon_3.groupby(['역명', '구분'], as_index=False).mean()
df_mon_4 = mon_4.groupby(['역명', '구분'], as_index=False).mean()
df_mon_5 = mon_5.groupby(['역명', '구분'], as_index=False).mean()
df_mon_6 = mon_6.groupby(['역명', '구분'], as_index=False).mean()
df_mon_7 = mon_7.groupby(['역명', '구분'], as_index=False).mean()
df_mon_8 = mon_8.groupby(['역명', '구분'], as_index=False).mean()
df_mon_9 = mon_9.groupby(['역명', '구분'], as_index=False).mean()
df_mon_10 = mon_10.groupby(['역명', '구분'], as_index=False).mean()
df_mon_11 = mon_11.groupby(['역명', '구분'], as_index=False).mean()
df_mon_12 = mon_12.groupby(['역명', '구분'], as_index=False).mean()



# 리스트로 구현하기
monlist_1 = df_mon_1.values.tolist()
monlist_2 = df_mon_2.values.tolist()
monlist_3 = df_mon_3.values.tolist()
monlist_4 = df_mon_4.values.tolist()
monlist_5 = df_mon_5.values.tolist()
monlist_6 = df_mon_6.values.tolist()
monlist_7 = df_mon_7.values.tolist()
monlist_8 = df_mon_8.values.tolist()
monlist_9 = df_mon_9.values.tolist()
monlist_10 = df_mon_10.values.tolist()
monlist_11 = df_mon_11.values.tolist()
monlist_12 = df_mon_12.values.tolist()



# while 문과 if 문을 이용하여 시스템 만들기
year=[monlist_1, monlist_2 ,monlist_3,monlist_4,monlist_5,monlist_6,monlist_7,monlist_8,monlist_9,monlist_10,monlist_11,monlist_12]

while True:
    month = int(input("몇 월?(정수로 입력하시오.) 검색을 멈추려면 0을 입력하시오. "))
    if month == 0:
        print("시스템을 종료합니다.")
        break

    time = int(input("시간대는? (6~24시 중 하나를 정수로입력하시오.) "))
    up = int(input("승차하실 역 번호를 입력하시오. "))
    down = int(input("하차하실 역 번호를 입력하시오. "))

    if month <0 or month > 12:
        print("Error")
        continue
    elif time > 23 or time < 6:
        print("Error")
        continue
    else:
        a = year[month-1]
        for i in range(0,len(a)):
            if a[i][3] == up :     # 승차 관련
                b = a[i]  # 입력한 역의 데이터들만 모아서 b에 저장
            if a[i][3] == down :   # 하차 관련
                c = a[i]  # 입력한 역의 데이터들만 모아서 c에 저장

        # 승차역 등급 매기기
        if b[time-2] < 100 :
            grade1 = "1등급"
        elif 100<=b[time-2]<300:
            grade1 = "2등급"
        elif 300<b[time-2]<500:
            grade1 = "3등급"
        elif 500<=b[time-2]<700:
            grade1 = "4등급"
        else:
            grade1 = "5등급"

        # 하차역 등급 매기기
        if c[time-2] < 100 :
            grade2 = "1등급"
        elif 100<=c[time-2]<300:
            grade2 = "2등급"
        elif 300<c[time-2]<500:
            grade2 = "3등급"
        elif 500<=c[time-2]<700:
            grade2 = "4등급"
        else:
            grade2 = "5등급"
        print("승차하실",b[0],"역의", month,"월",time,"시의 평균 인원은",b[time-2],"이며, ",grade1, "입니다.")  # 리스트를 통해 알 수 있다.
        print("하차하실",c[0],"역의",month,"월 ",time,"시의 평균 인원은",c[time-2],"이며, ",grade2, "입니다.")


# print(mon_1[mon_1['역번호'].isin(['95'])])
