debug = 0
n, m = map(int, input().split())
arr = list()
for i in range(n):
	arr.append(list(input()))

if debug:
	print(arr)
canIrepeat=0

def PointingEachOther(char1, char2, mode):
	# char1 is always in left or up then char2
	if char1 == ">" and char2 == "<" and mode == 1: 
		return 1
	if char1 == "v" and char2 == "^" and mode == 2:
		return 1
	return 0

def horizontal(startJ,startI):
	canBeRotated = 0
	alreadyRotated = 0
	
	j = startJ
	i = startI

	while(1):
		if(arr[j][i] == "<"):
			alreadyRotated += canBeRotated
		elif (arr[j][i] == ">"):
			canBeRotated += 1
		else:
			break
		if (i == len(arr[0]) - 1):
			break
		else:
			i += 1
			
	return alreadyRotated, j, i

def vertical(startJ, startI):
	canBeRotated = 0
	alreadyRotated = 0
	
	j = startJ
	i = startI
	
	while(1):
		if(arr[j][i] == "^"):
			alreadyRotated += canBeRotated
		elif (arr[j][i] == "v"):
			canBeRotated += 1
		else:
			break
		if (j == len(arr) - 1):
			break
		else:
			j += 1
	return alreadyRotated,  j, i

answer = 0

for j in range(len(arr)):
	i = 0
	while (i < len(arr[0])):
		if debug:
			print("search start : " + str(j) + " " + str(i))
		respond = horizontal(j,i)
		if debug:
				print(respond)
		if i == respond[2]:
			i += 1
		else:
			i = respond[2]
		answer += respond[0]

if debug:
	print(answer)

for i in range(len(arr[0])):
	j = 0
	while (j < len(arr)):
		if debug:
			print("search start : " + str(j) + " " + str(i))
		respond = vertical(j,i)
		if debug:
				print(respond)
		if j == respond[1]:
			j += 1
		else:
			j = respond[1]
		answer += respond[0]

print(answer)
# https://codeforces.com/gym/103150/problem/B
