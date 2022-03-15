x,y,w,h = map(int,input().split()) #x,y는 (x,y)에서 (0,y)or (x,0) 까지
mx = w-x #mx는 (x,y) 에서 (w,y)까지
my = h-y #my는 (x,y) 에서 (x,h)까지
print(min(x,y,mx,my))
      
