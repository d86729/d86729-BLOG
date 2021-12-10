input()
arr = list(map(int,input().split()))
M = max(arr)

sum = 0
for idx in range(len(arr)):
  arr[idx] = arr[idx] / M * 100
  sum += arr[idx]
print(sum / len(arr))

