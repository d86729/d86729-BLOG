usage = dict()
txt = input()
txt = list(txt.upper())

for idx in txt:
  if idx not in usage:
    usage[idx] = 1
  else:
    usage[idx] += 1

nums = []
for idx in usage:
  nums.append(usage[idx])

nums.sort()
nums.reverse()

if len(nums) == 1:
  print(txt[0])
elif nums[0] == nums[1]:
  print('?')
else:
  for idx in usage: 
    if usage[idx] == nums[0]:
      print(idx)
      break