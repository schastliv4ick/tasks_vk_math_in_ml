def rec(a, Dig, deep):
    for i in range(Dig + 1):
        if len(a) < deep - 1:
            a.append(i)
            rec(a, Dig, deep)
        if deep-1  == len(a):
            if len(a) != 0:
                print(" ".join(map(str, a)), i)
            else:
                print(i)
    if len(a) > 0:
        a.pop()




def sist(a, st):
    s = ''
    while a != 0:
        s = str(a % st) + s
        a = a // st
    s = '0'*(st - len(s))+s
    return s



N, maxDig = map(int, input().split()) # размер размещения и максимальная цифра

cnt = (maxDig+1)**N
a = []
rec(a, maxDig, N)

#for i in range((maxDig+1)**(N)):
#    print(sist(i, N))