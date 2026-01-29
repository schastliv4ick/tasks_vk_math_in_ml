def rec(a, Dig, deep):
    for i in range(Dig + 1):
        if len(a) < deep - 1:
            a.append(i)
            rec(a, Dig, deep)
        if deep-1  == len(a):
            print("".join(map(str, a))+str(i))
    if len(a) > 0:
        a.pop()



N, maxDig = map(int, input().split()) # размер размещения и максимальная цифра

cnt = (maxDig+1)**N
a = []
rec(a, maxDig, N)