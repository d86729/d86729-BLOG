from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
comb_set = list(combinations(cards, 3))

set = list()
for i in range(len(comb_set)):
    tmp = 0
    tmp += comb_set[i][0]
    tmp += comb_set[i][1]
    tmp += comb_set[i][2]
    if(tmp > M):
        tmp = -1
    set.append(tmp)

print(max(set))
#http://boj.kr/326ad9b374664293b68b575c74ef20ec
