debug = 0


def io():
    candisum = 0
    num_2 = 0
    num_1 = 0

    k = int(input())
    arr = list(map(int, input().split()))
    if (debug):
        print(arr)

    # how many 1/2 grams?
    for i in range(len(arr)):
        candisum = arr[i] + candisum
        if (arr[i] == 1):
            num_1 += 1
        else:
            num_2 += 1

    if debug:
        print("Candisum : " + str(candisum))
        print("Candisum // 2 = " + str(candisum // 2))
        print("num_1 = " + str(num_1))
        print("num_2 = " + str(num_2))

    if candisum % 2 == 1:  # candisum is an odd number
        return "NO"
    else:  # even number
        half = candisum // 2
        ones_try = 0

    if half % 2 == 1:
        ones_try = 1-2
    else:  # even number
        ones_try = 0-2

    while 1:
        ones_try += 2
        if num_1 < ones_try:
            ones_try -= 2
            break
        else:
            if num_2 >= (half - ones_try) // 2:
                break
            else:
                continue

    twos_try = (half - ones_try) // 2
    if debug:
        print("ones for the half : " + str(ones_try))
        print("twos for the half: " + str(twos_try))
    if ones_try + 2 * twos_try == half and ones_try >= 0:
        return "YES"
    else:
        return "NO"


n = int(input())
# if debug:
#    n = 1
for _ in range(n):
    print(io())
