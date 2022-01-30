N = int(input())
li = list(map(int,input().split()))
li.sort()
ans = 0
cnt = 0
for num in li:
    ans += (N-cnt) * num
    cnt += 1
print(ans)
