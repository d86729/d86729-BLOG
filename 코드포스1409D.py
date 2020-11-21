debug =0
def NumToArr(number):
	arr = str(number)
	ret = []
	for i in range(len(arr)):
		ret.append(int(arr[i]))
#	if(debug):
#		print("ret : "+str(ret))
	return ret
	
def DightSum(num):
	arr = NumToArr(num)
	sumret =0
	for i in range(len(arr)):
		sumret += arr[i]
	return sumret

def RoundUp(n,backzero):
	pl = 10 ** backzero
	if(backzero==0):
		return n
	n = ((n + pl) // pl) * pl
	if(debug):
		print("Round-up : "+str(n))
	return n

def Test(n,WantSum):
	i = 0
	NextRoundUp = 10 ** 25 -1
	while(1):
		if(DightSum(NextRoundUp) <= WantSum):
			break
		NextRoundUp = RoundUp(n,i)
		i += 1
	print(NextRoundUp - n)
	return
	
k = int(input())
for i in range(k):
	a,b = list(map(int, input().split()))
	Test(a,b)
