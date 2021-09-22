#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구하고
#쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
month = now.month

#조건문으로 계절 확인

if 3 <= month <= 5 :
    print("이번달은 {}월로 봄입니다.".format(month))

elif 6<= month <= 8 :
    print("이번달은 {}월로 여름입니다.".format(month))
    
elif 9<= month <=11 :
    print("이번달은 {}월로 가을입니다.".format(month))

else  :
    print("이번달은 {}월로 겨울입니다.".format(month))
    
time = now.hour
minute = now.minute

print("지금은",time,"시",minute,"분 입니다.")
