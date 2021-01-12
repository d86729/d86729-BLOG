N = int(input())
array = dict()
num = 1
k = 1
while num <= 10 ** 10:
    #print(str(num) + " : " + str(k - 1))
    array[k - 1] = num
    num += 6 * k
    k += 1
# print(array)
if N == 1:
    print(1)
for i in range(len(array)-1):
    if array[i] < N <= array[i + 1]:
        print(i + 2)
        break
