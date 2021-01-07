dict_2 = {}
def how_many_2(n):
    if n in dict_2:
        return dict_2[n]
    else:
        cuts = 0
        while(1):
            if(n % (2 ** cuts) == 0):
                cuts += 1
                continue
            else:
                break
        dict_2[n] = cuts-1
        return cuts-1

def io():
    w, h, n = map(int, list(input().split()))
    W = how_many_2(w)
    H = how_many_2(h)
    return ((2 ** W) * (2 ** H) >= n)

n = int(input())
for _ in range(n):
    if(io()):
        print("YES")
    else:
        print("NO")
