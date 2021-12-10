t_case = int(input())
answer = 0
for _ in range(t_case):
  N = list(input())
  N.append('?')
  n = []
  
  for i in range(len(N)-1):
    if N[i] != N[i+1]:
      n.append(N[i])
    else: #같으면
      continue
  #print(n)

  d = []
  flag = 1
  for idx in n:
    if idx not in d:
      d.append(idx)
    else:
      flag = 0
  if flag == 1:
    answer += 1

print(answer)
