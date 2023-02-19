# pandas 불러오기 
import pandas as pd 

# key: value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장 
dict_dat = {'a': 1, 'b':2, 'c':3}

#판다스 Series() 함수로 dictionary를 Series로 변환, 변수 sr에 저장 
sr = pd.Series(dict_dat)

#sr의 자료형 출력
print(type(sr))
print('\n')
# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)
print(sr[0])

# 리스트를 시리즈로 변환하여 변수 sr로 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr) 

inx = sr.index
val = sr.values
print(inx)
print('\n')
print(val)

#튜플을 시리즈로 변환(인덱스 옵션 지정)
tup_data= ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

#시리즈 원소 선택 
print(sr[0])
print(sr['이름'])

print(sr[[1,2]])
print('\n')
print(sr[['생년월일', '성별']])

print(sr[1 : 2])
print('\n')
print(sr['생년월일' : '성별'])

