T_case = int(input())

for _ in range(T_case):
  ln, str = input().split()
  ln = int(ln)
  str = list(str)
  #print(f'{type(ln)} {type(str)}')

  for idx in str:
    print(idx * ln, end='')
  print()