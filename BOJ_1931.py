s_li = []
cnt = 0
N = int(input())
for q in range(N):
    s, e = map(int, input().split())
    s_li.append([e,s])
s_li.sort()
useable = 0
for meet in s_li:
    if meet[1] < useable:
        continue
    else:
        cnt += 1
        useable = meet[0]
print(cnt)
