
keyboard_l = {'z':[0,0],'x':[1,0],'c':[2,0],'v':[3,0],'a':[0,1],'s':[1,1],'d':[2,1],'f':[3,1],'g':[4,1],'q':[0,2],'w':[1,2],'e':[2,2], 'r':[3,2],'t':[4,2]}
keyboard_r = {'b':[4,0],'n':[5,0],'m':[6,0],'h':[5,1],'j':[6,1],'k':[7,1],'l':[8,1],'y':[5,2],'u':[6,2],'i':[7,2],'o':[8,2],'p':[9,2]}
sl,sr = map(str,input().split())
l = keyboard_l[sl]
r = keyboard_r[sr]
d = 0
stn = input()
result = []

for i in stn:
    if i in keyboard_l : #왼쪽 손 키보드(자음)
        nl = keyboard_l[i]
        d += abs(l[0]-nl[0])+abs(l[1]-nl[1])+1 # 이동하는 시간 + 키 누르는데시간
        l = nl
        
    else :
        nr = keyboard_r[i] #오른쪽손 키보드(모음)
        d+= abs(r[0]-nr[0])+abs(r[1]-nr[1])+1
        r = nr

print(d)
