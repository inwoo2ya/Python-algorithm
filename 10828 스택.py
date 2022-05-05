import sys
n = int(input())

stack = []
for _ in range(n):
    s = sys.stdin.readline().split()
    i = 0

    if len(s) == 2 :
        i = s[1]

    s = s[0]
    if s == 'push':
            stack.append(i)
    if s == 'pop' :
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif s== 'size':
        print(len(stack))
    elif s=='empty':
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif s=='top':
        if len(stack) == 0:
            print(-1)
        else:    
            print(stack[-1])
