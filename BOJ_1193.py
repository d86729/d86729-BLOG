x = int(input())
guess_n = round((2*x) ** (1/2))
better_n = -1
atm = 0
flg = 0
mi = 0
mx = 0
while(1):
  for f in range(2):
    if f == 0:
      better_n = guess_n + atm
      if better_n <= 0:
        continue
    else:
      better_n = guess_n - atm
      if better_n <= 0:
        continue
    #print(better_n) #추리된 better_n 값은 여기서 정해짐
      # better_n으로 하는 계산은 여기서부터
    mi = (better_n - 1) * (better_n - 2) // 2 + 1
    mx = (better_n) * (better_n-1) // 2
    #print(better_n, mi,mx)
    if mi <= x <= mx:
      flg = 1
    if flg == 1:
      break
      #여기까지
  #루프 마지막에 둘 것.
  if flg == 1:
    break
  atm += 1
  better_n = guess_n

if better_n % 2 == 0: 
  print(f'{better_n-(1+x-mi)}/{1+x-mi}')
else:
  print(f'{1+x-mi}/{better_n-(1+x-mi)}')
