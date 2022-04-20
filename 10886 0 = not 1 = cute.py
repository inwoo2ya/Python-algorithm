n = int(input())
a = 0 #찬성
b = 0 #반대
for i in range(n) :
    c = int(input())
    if c == 1:
        a +=1
    elif c==0 :
        b +=1

if a>b :
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
