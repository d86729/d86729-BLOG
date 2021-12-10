import sys
str = list(sys.stdin.readline().rstrip())
#print(str)

for i in range(ord('z') - ord('a')+1):
  #print(chr(ord('a')+i))
  char = chr(ord('a')+i)
  answer = -1
  try:
    answer = str.index(char)
  except:
    pass
  print(answer, end=' ')