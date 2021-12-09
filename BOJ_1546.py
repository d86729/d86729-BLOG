input()
arr = list(map(int,input().split()))
M = max(arr)

for idx in range(len(arr)):
  arr[idx] = arr[idx] / M * 100
print(arr)