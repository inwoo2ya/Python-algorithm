n = int(input())

a=1
d=6
room=1
if n == 1:
    print(1)
else :
    while True :
        a = a+d
        room+=1
        if n <= a :
            print(room)
            break
        d += 6
