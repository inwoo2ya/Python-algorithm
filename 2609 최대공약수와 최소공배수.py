a,b = map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    result = (a*b)//gcd(a,b)
    return result

print(gcd(a,b))
print(lcm(a,b))
