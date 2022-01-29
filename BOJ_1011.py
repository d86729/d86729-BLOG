import math
def solve(dist):
    r_dist = math.floor((dist ** (0.5)))
    #print(r_dist)
    ans = 2 * r_dist - 1
    #print(ans)
    if(dist-(r_dist ** 2) != 0):
        remain = dist - (r_dist ** 2)
        if (remain % r_dist ==0):
            ans += remain // r_dist
        else:
            ans += remain// r_dist + 1
    return ans
t= int(input())
for q in range(t):
    a, b = map(int, input().split())
    print(solve(b-a))
