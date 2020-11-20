debug = 0

def divisor_arr(n):# n의 약수를 배열로 반환
	div = list()
	for i in range(n):
		if(n % (i+1) ==0):
			div.append(i+1)
	if(debug):
		print("div : " + str(div))
	return div
	
def determine_minustimes(arr,small,big,dist):
	if(arr[0] % dist ==0):
		SmallLimit = arr[0] // dist -1
	else:#배열의 모든 요소를 dist만큼 뺄 때, 음수인 요소가 없는 한에서 반복할 수 있는 최대한의 횟수
		SmallLimit= arr[0] // dist
	if(debug):
		print("SmallLimit : "+str(SmallLimit))
	BigLimit = (arr[-1] - big) // dist
	if(debug):
		print("BigLimit : "+str(BigLimit)) # big값이 수열에 남아 있기까지의 (동 연산의)최대한의 횟수
	return min(SmallLimit,BigLimit)
	
def restore(arrlen,small,big,dist):
	minustimes = 0
	tiles = (big-small) // dist + 1 # small과 big 사이 연결하는 칸 수
	if(tiles > arrlen):
		return [987654321]# restore impossible
	else:
		arr = list()
		for q in range(arrlen):
			arr.append(small +  dist * q)
		if(debug):
			print("dist : "+str(dist))
		minustimes = determine_minustimes(arr,small,big,dist)
		for q in range(arrlen):
			arr[q] -= dist * minustimes
		return arr 

def test(arrlen, small, big):#메인 함수
	div = divisor_arr(big-small)#약수 구하기
	use_able = list()#small, big을 포함하는 등차수열의 공비로 사용 가능한 약수를 담는 곳
	restored = list()#사용 가능한 약수로 배열 복구
	
	for i in range(len(div)):
		if(small % div[i] == big % div[i]):
			use_able.append(div[i])

	for option in range(len(use_able)):
		restored.append(restore(arrlen,small,big,use_able[option]))#배열 복구
	if(debug):
		print("restored : " +str(restored))
	
	best = 987654321
	best_loc = -1
	
	for q in range(len(restored)):#후보군 중 선택
		if(best > (restored[q][-1])):
			best = restored[q][-1]
			best_loc = q
			
	for q in range(len(restored[best_loc])):
		print(restored[best_loc][q], end=' ')

	return

def IO():#테스트 케이스 1개의 입출력 전담
	arr = list(map(int,input().split()))
	test(arr[0],arr[1],arr[2])
	print()
	if(debug):
		print("---------------")
	return
	
tc = int(input())
for _ in range(tc):
	IO()
