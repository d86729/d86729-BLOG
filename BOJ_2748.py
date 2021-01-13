pibo = list()
pibo.append(0)
pibo.append(1)
pibo.append(-1)
# index out of range 해결을 위해, 미리 임의의 값을 리스트에 넣어둔다.
n = int(input())
for i in range(n):
    pibo[i+2] = pibo[i] + pibo[i+1]
    pibo.append(-1)

print(pibo[n])
