debug = 0
arr = dict()
arr[1] = [0, 1]
# 1자리 수 이친수 중 마지막 자리가 0인 것은 0개, 1인 것은 1개이다.
n = int(input())
di = 2
if debug:
    print(arr[1])
for i in range(n + 2):
    arr[di] = [arr[di-1][1] + arr[di-1][0], arr[di-1][0]]
    if debug:
        print(arr[di])
    di += 1

print(arr[n][0] + arr[n][1])