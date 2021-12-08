divs = []
for i in range(10):
  num = int(input())
  div = num % 42
  if div not in divs:
    divs.append(div)
  
print(len(divs))
