
cost_list = []
def input2(n):
    l = list(map(int, input().split())) 
    c = list(map(int, input().split()))
    c.pop()# 마지막 도시의 기름값은 상관없음.
    cnt = 0
    for i in range(n): # 가장 왼쪽 도시는 0, 나머지 도시들은 가장 왼쪽 도시와 떨어진 거리만큼에 해당하는 값으로 부여
        cost_list.append([c[i], cnt])
        cnt += l[i]
    cost_list.sort()
    if debug:
        print(cost_list)
    return cnt
    
def solve(target):# cnt(input2애서의) = target = 목적지의 위치
    ans = 0
    for idx in cost_list:
        if target <= idx[1]:
            continue
        ans += (target- idx[1]) * idx[0]
        target = idx[1]
    return ans

q = int(input())
print(solve(input2(q-1)))
# 전체 비용은 다음과 같다.
# 가장 기름값이 저렴한 도시까지 가는 비용 +
# 시작점부터 가장 기름값이 저렴한 도시까지 가는 비용.
