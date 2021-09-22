dialog = list(input().upper())
sum = 0
for n in dialog :
    if n == "A" or n =="B" or n =="C" :
        sum = sum+3
    elif n=="D" or n =="E" or n=="F" :
        sum = sum+4
    elif n=="G" or n=="H"  or n=="I" :
        sum = sum+5
    elif n=="J" or n=="K" or n=="L" :
        sum = sum+6
    elif n=="M" or n=="N" or n=="O" :
        sum = sum+7
    elif n=="P" or n=="Q" or n=="R" or n=="S":
        sum = sum+8
    elif n=="T" or n=="U" or n=="V" :
        sum = sum+9
    elif n=="W" or n=="X" or n=="Y" or n=="Z" :
        sum =sum +10
    else :
        sum = sum+11
print(sum)
