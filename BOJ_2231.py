def num_len(num):
    di = 1
    mi = 1
    ma = 10
    while 1:
        if mi <= num < ma:
            break
        else:
            mi *= 10
            ma *= 10
            di += 1
    return di
def func(num):
    di = num_len(num)
    ans = num
    for i in reversed(range(di)):
        ans += num % 10 ** (i+1) // 10 ** i
    return ans

n = int(input())

flag = 1
p = n - 1000
if p < 1:
    p = 1

for _ in range(2000):
    if func(p) == n:
        print(p)
        flag = 0
        break
    p += 1

if flag:
    print(0)
