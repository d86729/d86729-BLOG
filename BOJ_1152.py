import sys
txt = list(sys.stdin.readline().strip())

if txt == []:
  print(0)
else:
  cnt = 1
  for t in txt:
    if t == ' ':
      cnt += 1
  print(cnt)
