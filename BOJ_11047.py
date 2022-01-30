coins= []
def data():
    N, K = map(int, input().split())
    for q in range(N):
        kw = int(input())
        coins.append(kw)
    coins.reverse() # 큰 금액 동전이 앞으로 감
    return K

debug = 0
def solve(K):# K는 동전으로 만들 금액이다.
    idx = 0
    ans = 0 
    while(K>0):
        if(coins[idx]>K): # 동전 1개 가치 > 만들어야 할 금액
            idx +=1 # 한 단계 작은금액 동전을 선택하기로 함
            continue
        ans += K // coins[idx]
        K -= (K // coins[idx]) * coins[idx]
        if debug:
        	print(ans)
        idx += 1
    print(ans)
    return
solve(data())
