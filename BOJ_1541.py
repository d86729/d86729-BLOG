neg = 1
debug = 1
ans = 0
num = 0
numlist = ['0','1','2','3','4','5','6','7','8','9']
wd = input()
for idx in wd:
	if idx in numlist:
		num = num*10+numlist.index(idx)
		#print(numlist.index(idx))
	elif idx == '+':
		ans += num * neg
		num = 0
	else:
		ans += num * neg
		num = 0
		neg = -1

ans += num *neg
print(ans)
