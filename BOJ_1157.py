usage = dict()

txt = input()
txt = list(txt.upper())
print(type(txt))

for idx in str:
  if idx not in usage:
    usage[idx] = 1
  else:
    usage[idx] += 1

print(usage)
