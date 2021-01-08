debug = 0
mem = dict()

def solve(arr):
    best_score = -1

    for rev in range(len(arr)):
        i = len(arr) - rev - 1
        if debug:
            print("----------------------------------")
            print("i = " + str(i))
        current_score = 0

        idx = i
        while 1:
            if debug:
                print("reach(arr, " + str(idx) + ", " + str(current_score) + ")")

            if idx not in mem:
                data = arr[idx]
            else:
                if debug:
                    print("using mem[" + str(idx) + "] = " + str(mem[idx]))
                current_score += mem[idx]

                # writing mem, then break the loop
                if debug:
                    print("writing mem / mem[" + str(idx) + "] = " + str(current_score))
                mem[i] = current_score
                break

            current_score += data

            if idx + data >= len(arr):

                # writing mem, then break the loop
                if debug:
                    print("writing mem / mem[" + str(idx) + "] = " + str(current_score))
                mem[i] = current_score
                break

            idx += arr[idx]

        if current_score > best_score:
            best_score = current_score
            if debug:
                print("new best score!")
                print("best score = "+str(best_score))

    print(best_score)


def io():
    input()
    arr = list(map(int, input().split()))

    solve(arr)


if debug:
    n = 1
else:
    n = int(input())

for _ in range(n):
    io()
    mem.clear()
