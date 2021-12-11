t = int(input())
for i in range(t):
  H, W, N = map(int,input().split())
  Floor = str((N-1) % H + 1)
  Room = str((N-1) // H + 1)
  if len(Room) == 1:
    Room = '0' + Room
  print(Floor+Room)