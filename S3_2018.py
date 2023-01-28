#1. factory
#2. conceptual map
rowcol = input().split()
x = int(rowcol[0])
y = int(rowcol[1])

startPosition = None
factoryMap = []
conceptualmap = []

for i in range(x):
  row = input()
  if startPosition is None:
    start_col = row.find('S')  
    # find returns -1 if it doesnt find what you asked in this case 'S'
    if start_col != -1:
      startPosition = [i, start_col]
  factoryMap.append(list(row))
  conceptualmap.append([-1] * y)

for i in range(x):
  for j in range(y):
    if factoryMap[i][j] == 'C':
      #check down
      count = 0
      while True:
        if factoryMap[i + count][j] in ['.', 'S']:
          factoryMap[i + count][j] = '*'
        elif factoryMap[i + count][j] == 'W':
          break
        count += 1

      #check up
      count = 0
      while True:
        if factoryMap[i - count][j] in ['.', 'S']:
          factoryMap[i - count][j] = '*'
        elif factoryMap[i - count][j] == 'W':
          break
        count += 1

      #check right
      count = 0
      while True:
        if factoryMap[i][j + count] in ['.', 'S']:
          factoryMap[i][j + count] = '*'
        elif factoryMap[i][j + count] == 'W':
          break
        count += 1

      #check left
      count = 0
      while True:
        if factoryMap[i][j - count] in ['.', 'S']:
          factoryMap[i][j - count] = '*'
        elif factoryMap[i][j - count] == 'W':
          break
        count += 1

queue = [startPosition]  #1. need a queue for BFS
conceptualmap[startPosition[0]][startPosition[1]] = 0

while len(queue) != 0:  #2. while loop for BFS
  currentCell = queue.pop(0)  #3. extract the first item
  r = currentCell[0]
  c = currentCell[1]
  #4. check the cell and append the children
  #checkup
  if (conceptualmap[r-1][c]==-1 or (conceptualmap[r][c]<conceptualmap[r-1][c] and factoryMap[r][c]=='U' or conceptualmap[r][c]+1<conceptualmap[r-1][c]) and factoryMap[r-1][c] not in ['W','*'] and factoryMap[r][c] not in ['D', 'L', 'R']):
    if factoryMap[r][c] not in ['U', 'D', 'L', 'R']:
      conceptualmap[r - 1][c] = conceptualmap[r][c] + 1
    else:  #case when we are on a conveyer
      conceptualmap[r - 1][c] = conceptualmap[r][c]
    queue.append([r - 1, c])
  #check down
    
  if (conceptualmap[r+1][c]==-1 or (conceptualmap[r][c]<conceptualmap[r+1][c] and factoryMap[r][c]=='D' or conceptualmap[r][c]+1<conceptualmap[r-1][c]) and factoryMap[r+1][c] not in ['W','*'] and factoryMap[r][c] not in ['U', 'L', 'R']):
    if factoryMap[r][c] not in ['U', 'D', 'L', 'R']:
      conceptualmap[r + 1][c] = conceptualmap[r][c] + 1
    else:  #case when we are on a conveyer
      conceptualmap[r + 1][c] = conceptualmap[r][c]
    queue.append([r + 1, c])

    
  #check left
  if (conceptualmap[r][c+1]==-1 or (conceptualmap[r][c]<conceptualmap[r][c+1] and factoryMap[r][c+1]=='L' or conceptualmap[r][c]+1<conceptualmap[r][c+1]) and factoryMap[r][c+1] not in ['W','*'] and factoryMap[r][c] not in ['D', 'U', 'R']):
    if factoryMap[r][c] not in ['U', 'D', 'L', 'R']:
      conceptualmap[r][c + 1] = conceptualmap[r][c] + 1
    else:  #case when we are on a conveyer
      conceptualmap[r][c + 1] = conceptualmap[r][c]
    queue.append([r, c + 1])
  #check right
  if (conceptualmap[r][c-1]==-1 or (conceptualmap[r][c]<conceptualmap[r][c-1] and factoryMap[r][c]=='R' or conceptualmap[r][c]+1<conceptualmap[r][c-1]) and factoryMap[r][c-1] not in ['W','*'] and factoryMap[r][c] not in ['D', 'L', 'U']):
    if factoryMap[r][c] not in ['U', 'D', 'L', 'R']:
      conceptualmap[r][c - 1] = conceptualmap[r][c] + 1
    else:  #case when we are on a conveyer
      conceptualmap[r][c - 1] = conceptualmap[r][c]
    queue.append([r, c - 1])

for r in range(x):
  for c in range(y):
    if factoryMap[r][c] == '.':
      if factoryMap[startPosition[0]][startPosition[1]] == '*':
        print(-1)
      else:
        print(conceptualmap[r][c])
    elif factoryMap[r][c] == '*' and [r][c] != startPosition:
      print(-1)

    #if factoryMap[i][j] == "C" then check up/down/left/right in factoryMap update factory map spot to *
#     if factoryMap[i][j] == "C":
#       factoryMap[i][j + 1] = "*"
#       factoryMap[i][j - 1] = "*"

# print(factoryMap)

#for row

#    for col
#        while
#if cam *
#              check up/dpwn/left/right update factory map spot to *
#queue startPosition
#conceptualmap[startx][starty] = 0
#BFS

