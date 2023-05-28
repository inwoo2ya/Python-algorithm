s = '1 2 3 4 B B 42 B F F'
page = []
currentPage = []
nextPage =[]
total = []
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
        nextPage = []

e = list(set(page))
for i in e:
    total.append(page.count(i))

print(max(total))
