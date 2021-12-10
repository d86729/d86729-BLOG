STR = input()
conv = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for idx in conv:
  STR = STR.replace(idx, '?')
print(len(STR))