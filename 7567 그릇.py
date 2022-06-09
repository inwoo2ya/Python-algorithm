bowl = list(input())
height = 0
for i in range(len(bowl)):
    if i == 0:
        height +=10 # 첫번째 그릇은 10cm
    elif bowl[i] == bowl[i-1]: # i-1번째 그릇과 i그릇이 같으면 5cm (포개어지면)
        height +=5
    else: # i-1번째 그릇과 i 그릇이 다르면 10cm
        height+=10

print(height)
        
