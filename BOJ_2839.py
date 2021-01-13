debug = 0
ln = 5001
INF = 987654321

array = list()
for _ in range(ln):
    array.append(-1)
array[3] = 1
array[5] = 1

for i in range(ln):
    if debug:
        print("i = " + str(i))

    a = INF
    b = INF
    flag = 0
    if i - 3 > 0:
        if array[i-3] != -1:
            if debug:
                print(3333333333)
            flag = 1
            a = array[i - 3] + 1
    if i - 5 > 0:
        if array[i - 5] != -1:
            if debug:
                print(55555555555)
            flag = 1
            b = array[i - 5] + 1
    if flag:
        c = min(a, b)
        if debug:
            print(c)
        array[i] = c
        if debug:
            print(array)

N = int(input())
print(array[N])