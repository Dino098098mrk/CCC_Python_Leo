dp = [[[[False for d in range (31)] for c in range(31)] for b in range(31)] for a in range(31)]
moves = [[1,1,1,1],[0,3,0,0],[0,0,2,1],[2,1,0,2],[1,0,0,1]]


#True (0) patrick wins
#False (1) roland wins
def whoWins(a,b,c,d):
  if a<0 or b < 0 or c<0 or d<0:
    return False
  else:
    return not dp[a][b][c][d]

for a in range(31):
  for b in range(31):
    for c in range(31):
      for d in range(31):
        for m in moves:
          if whoWins(a-m[0],b-m[1],c-m[2],d-m[3]):
            dp[a][b][c][d]=True
            
output = []
times = int(input())

for i in range(times):
  card = str(input())
  card = card.split()
  a = int(card[0])
  b = int(card[1])
  c = int(card[2])
  d = int(card[3])
  print("cards are",a,b,c,d)
  if dp[a][b][c][d] == True:
    output.append("Patrick")
  else:
    output.append("Roland")


for i in output:
  print(i)