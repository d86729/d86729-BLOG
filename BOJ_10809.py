import sys
str = sys.stdin.readline().rstrip()
#print(str)

for i in range(ord('z') - ord('a')+1):
  #print(chr(ord('a')+i))
  char = chr(ord('a')+i)
  answer = str.index(char)
  print(answer)