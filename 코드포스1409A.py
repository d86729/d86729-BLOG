t = int(input())
for i in range(t):
  a,b = map(int,input().split())
  dis = abs(b-a)
  if(dis % 10 ==0):
    print(dis // 10)
    continue
  else:
    print(dis // 10 + 1)
    continue
