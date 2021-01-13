debug = 0
# 숫자 N을 만드는 방법의 수 = (N - 1을 만드는 방법의 수) + (N - 2에 대한 방법의 수) + (N - 3에 대한 방법의 수)
table = {0: 1, 1: 1}
complete = 1
T = int(input()) # 테스트 케이스의 숫자
for _ in range(T): # 각 테스트 케이스마다
    N = int(input())
    for i in range(N+1):
        if i <= complete: # 이미 계산한 부분은
            continue # 건너뛰기
        ans = 0
        if debug:
            print("i = " + str(i))
        if i - 1 >= 0: # i - 1 < 0 이면 index out of range
            ans += table[i-1]
        if i - 2 >= 0:
            ans += table[i-2]
        if i - 3 >= 0:
            ans += table[i-3]
        table[i] = ans
    if debug:
        print(table)
    complete = N # 어디까지 계산이 완료되었는지 표시
    print(table[N])
