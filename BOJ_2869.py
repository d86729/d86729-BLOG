import math
debug = 0
A, B, V = map(int, input().split())

D = (V-A)/(A-B) + 1
if debug:
  print(D)
print(math.ceil(D))