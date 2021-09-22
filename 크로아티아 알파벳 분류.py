a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha = input()

for n in a :
    alpha = alpha.replace(n,"@") #a 와 같은 문자열이 나오면 그부분만 "@"로 바꿔준다!

sum = len(alpha)
print(sum)
