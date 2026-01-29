def rec(a, Dig, deep):
    for i in range(Dig + 1):
        if len(a) < deep:
            a.append(i)
            rec(a, Dig, deep)
        if deep == len:
            for x in a:
                print(x)
            print(i, '\n')
    if len(a) > 0:
        a.pop()




def A():
    N = int(input()) # размер размещения
    maxDig = int(input()) # максимальная цифра
    cnt = (maxDig+1)**N
    a = []
    rec(a, maxDig, N)


A()