import sys
debug = 0
array_dict = dict()
# {배열에 든 값 : 중복된 횟수}
array_keys = list()
# [값 1, 값 2, 값 3, 값 4, ... ]


def turn(alice_score, bob_score, who_first, number):
    # number : array_keys[i]
    if debug:
        print(who_first + " takes the turn first!")
    if debug == 3:
        print("alice_score = " + str(alice_score))
        print("bob_score = " + str(bob_score))
        print("array_keys[i] = number = " + str(number))

    if number % 2 == 0:
        if debug >= 2:
            print("no points for bob!")
        who_grant_point = "Alice"
    else:
        if debug >= 2:
            print("no points for alice!")
        who_grant_point = "Bob"

    if array_dict[number] % 2 == 1 and who_grant_point == who_first:
        k = 1
    else:
        k = 0

    if debug:
        print(who_grant_point + " gets " + str(number * (array_dict[number] // 2 + k)) + " points!")

    if who_grant_point == "Alice":
        alice_score += number * (array_dict[number] // 2 + k)
    elif who_grant_point == "Bob":
        bob_score += number * (array_dict[number] // 2 + k)

    if debug:
        print("now, Alice : " + str(alice_score) + " VS Bob : " + str(bob_score))

    if array_dict[number] % 2 == 1:
        if who_first == "Alice":
            who_first = "Bob"
        else:
            who_first = "Alice"

    return alice_score, bob_score, who_first


def solve(num_keys):
    alice_score = 0
    bob_score = 0
    who_first = "Alice"

    if debug == 2:
        print(array_dict)
        print(array_keys)
        print("----------------------------")

    for i in range(num_keys):
        alice_score, bob_score, who_first = turn(alice_score, bob_score, who_first, array_keys[i])

    if alice_score > bob_score:
        print("Alice")
    elif alice_score < bob_score:
        print("Bob")
    else:
        print("Tie")
    return


def io():
    t = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(t):
        try:
            array_dict[arr[i]] += 1
        except:
            array_dict[arr[i]] = 1
            array_keys.append(arr[i])
    array_keys.sort()
    array_keys.reverse()

    solve(len(array_keys))
    # turn(0, 0, "Alice", 3)
    return


if debug >= 2:
    n = 1
else:
    n = int(input())

for _ in range(n):
    io()
    array_keys.clear()
    array_dict.clear()
