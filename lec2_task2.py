def rec1(a, Dig, deep):
    for i in range(Dig + 1):
        if len(a) < deep - 1:
            a.append(i)
            rec1(a, Dig, deep)
        if deep-1  == len(a):
            if len(a) != 0:
                s = " ".join(map(str, a)) + " " + str(i)
                rec2(a, Dig, deep, s)
                #print(" ".join(map(str, a)), i)
            #else:
                #print(i)
    if len(a) > 0:
        a.pop()


def rec2(a, Dig, deep, s):
    for i in range(Dig + 1):
        if len(a) < deep - 1:
            a.append(i)
            rec2(a, Dig, deep)
        if deep-1  == len(a):
            if len(a) != 0:
                print(s, " ".join(map(str, a)), i)
            else:
                print(s, i)
    if len(a) > 0:
        a.pop()

N, M = map(int, input().split()) # размер половины и макс. цифра
a = []

rec1(a, N, M)