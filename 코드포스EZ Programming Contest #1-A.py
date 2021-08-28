test_case = int(input())
for _ in range(test_case):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	M = max(arr)
	N = min(arr)
	print(M-N) if M-N >=0 else print(N-M)
#https://codeforces.com/gym/103150/problem/A
