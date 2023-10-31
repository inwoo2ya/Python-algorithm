s = '1 2 3 4 B B 42 B F F'
page = []  # 이동 페이지 경로
currentPage = [] #현재 페이지 
nextPage =[] # 다음 이동할 수 있는 페이지 
total = [] #페이지가 렌더링된 수 
for i in s.split():
    if i == 'B':
        if len(currentPage ) != 0 :
            nextPage.append(currentPage[-1])
            currentPage.pop()
            page.append(currentPage[-1])
            continue
    elif i == 'F':
        if len(nextPage) != 0 :
            page.append(nextPage[-1])
            currentPage.append(nextPage[-1])
            nextPage.pop()
            continue
    else:
        currentPage.append(i)
        page.append(i)
        nextPage = [] #홈페이지 이동 시 다음 페이지 초기화

e = list(set(page))
for i in e:
    total.append(page.count(i))

print(max(total)) #가장 많이 이동한(렌더링된) 페이지의 수

