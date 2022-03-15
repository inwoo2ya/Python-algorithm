h,m = map(int,input().split())
intime = int(input())

inhour = intime//60 #60으로 나눈 몫 (60분이 총 몇개인가)
m += (intime % 60)  #60으로 나누고난후 분 
h += inhour
if m > 59 :
    h += 1
    m -= 60
    
if h > 23 :
    h -= 24

print(h,m)
