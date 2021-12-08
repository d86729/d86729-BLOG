
import sys
lines = sys.stdin.readlines()

arr = []
for line in lines:
  arr.append(int(line))

k = max(arr)
print(k)
print(arr.index(k)+1)
