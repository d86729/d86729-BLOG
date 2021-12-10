N = list(input())
T = {}

dial = 2
cnt = 0

for i in range(ord('Z') - ord('A')+1):
    if dial == 7 or dial == 9:
        Thr = 4
    else:
        Thr = 3
        
    if cnt == Thr:
        cnt = 0
        dial += 1
        
    T[chr(i+65)] =  dial+1
    cnt += 1

sum = 0
for idx in N:
    sum += T[idx]
print(sum)