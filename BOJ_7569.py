from pprint import pprint
from collections import deque
move = [[1, 0, 0], [-1, 0, 0], [0, 1, 0],[0,-1, 0], [0,0,1], [0,0,-1]]
M, N, H = list(map(int, input().split()))
board = [[[-1 for i in range(M + 2)] for j in range(N + 2)] for k in range(H+2)] # 만들 때는 정순(가로, 세로, 높이)
grown = []
#board[3][2][1] = 0 
#수정할 때는 역순(높이, 세로, 가로)
for z in range(1,H+1,1):
  for y in range(1,N+1,1):
    l = list(map(int,input().split()))
    for x in range(1,len(l)+1,1):
      board[z][y][x] = l[x-1]
for z in range(1,H+1,1):
  for y in range(1,N+1,1):
    for x in range(1,M+1,1):
      if (board[z][y][x] == 1):
        grown.append((z,y,x)) # xyz 역순

def frash(queuelist):
  for queue in queuelist:
    ln = len(queue)
    for _ in range(ln):
      t = queue.popleft()
      for mov in move:
        posz = t[0] + mov[0]
        posy = t[1] + mov[1]
        posx = t[2] + mov[2]
        if (board[posz][posy][posx] == 0):
          queue.append((posz, posy, posx))
          board[posz][posy][posx] = 1
  return queuelist

tomato = []
for idx in grown:
  tomato.append(deque([idx]))

answer = 0
while True:
  ret = frash(tomato)
  cnt = 0
  for idx in ret:
    if idx:
      cnt += 1
  if cnt == 0:
    break
  answer += 1

err = 0
for z in range(1, H + 1, 1):
  for y in range(1, N + 1, 1):
    for x in range(1, M+1, 1):
      if board[z][y][x] == 0:
        err = 1
        break

if err:
  print(-1)
else:
  print(answer)
