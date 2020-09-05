#http://boj.kr/e0fee60c4b784fc1ba9bcb758f17f013
N = int(input())
numchk = "665"

for tmp in range(N):
    while(True):
        numchk = str(int(numchk) + 1)
        if "666" in numchk:
            break

print(numchk)
