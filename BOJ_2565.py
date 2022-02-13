N = int(input())
li = [[0,0]]
for q in range(N):
	li.append(list(map(int, input().split())))
li.sort(key=lambda x:x[0])
k= []
for idx in li:
	k.append(idx[1])

A = [0 for q in range(len(li))]


def lcs(d):
	for idx in range(1, N+1, 1):
		max = -1
		
		for i in range(0, idx, 1):
			if(d[i] < d[idx] and A[i] > max):
				max = A[i]
				
		A[idx] = max + 1
		
	M = -1
	for val in A:
		if(val > M ):
			M = val
	return (len(d)-1-M)
	
print(lcs(k))
