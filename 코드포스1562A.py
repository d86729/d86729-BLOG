def Func_2N(num):
	# 2n + 1 < num, return max n
	if (num-1 %2 == 0):
		return (num-1) // 2 -1
	else:
		return (num-1) // 2
debug = 0
# https://codeforces.com/contest/1562/problem/A
#print(Func_2N(9999999999))

def slowsolve(l, r):
#	print("==========")
	bestMod = -1
	for b in range(l,r+1):
		for a in range(b, r+1):
			if a % b > bestMod:
				bestMod = a % b
	print(bestMod)
	#print("==========")
	
T = int(input())
for _ in range(T):
	l, r = list(map(int, input().split())) #print(l,r)
	
	if(l <= 10 and r <= 10):
		slowsolve(l, r)
		continue
	
	# l is too high, then useless method.
	mod = Func_2N(r)
	if debug:
		print(str(2*mod+1) + " mod " + str(mod+1) + " = "+ str(mod))
	if l <= mod+1:
		print(mod)
	else:
		print(r % l)
