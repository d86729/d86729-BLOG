debug = 0
updownsum = 2
li = []
while(1):
  val = updownsum * (updownsum-1) // 2
  if updownsum > 10000000:
    break
  if debug:
    print(val)
  else:
    li.append(val)
  updownsum += 1
  
if not debug:
  print(len(li))