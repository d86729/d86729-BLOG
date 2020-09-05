money = 1000 - int(input())
used = 0
array = (500, 100, 50, 10, 5, 1)
def minus(coin):
    global used
    global money
    used += money // coin
    money -= (money // coin) * coin
    return

for i in range(len(array)):
    minus(array[i])
print(used)


#http://boj.kr/46ae51573e204def9d979cd39d4e023e
