
def a_first_minus(a,b,x,y,n,a_av,b_av):
	#print("a first minus -------")
	#a를 최대한 감산하고, 남은 횟수로 b를 감산
	
	if (a_av > n): #이동 횟수가 부족할 때
		a_av = n#어쩔 수 없이 많이 빼지 못한다
	a = a - a_av
	
	n = n - a_av
	#print("n= ",end="")
	#print(n)
	
	if (b_av >n):
		b_av = n;
	b = b - b_av
	
	return a*b
	
def b_first_minus(a,b,x,y,n,a_av,b_av):
	#print("b first minus -------")
	#b를 최대한 감산하고, 남은 횟수로 a를 감산
	
	if (b_av > n): #이동 횟수가 부족할 때
		b_av = n#어쩔 수 없이 많이 빼지 못한다
	b = b - b_av
	
	n = n - b_av
	#print("n = ",end="")
	#print(n)
	if (a_av >n):
		a_av = n;
	a = a - a_av
	
	return a*b

def test():
	arr = list(map(int,input().split()))
	#print("--‐-------------------------------")
	a = arr[0]
	b = arr[1]
	x = arr[2]
	y = arr[3]
	n = arr[4]
	a_av = a - x# a에 대해 최대로 감산 가능한 횟수
	b_av = b - y#b에 대한 최대 감산 가능 횟수
	
	if(a_av+b_av<=n):#그냥 횟수가 널널한 경우
		print((a-a_av)*(b-b_av))
		return
	else:
		case1 = a_first_minus(a,b,x,y,n,a_av,b_av)
		case2 = b_first_minus(a,b,x,y,n,a_av,b_av)
		if(case1 <= case2):
			print(case1)
			return
		else:
			print(case2)
			return

	return
	
t = int(input())
for _ in range(t):
	test()
