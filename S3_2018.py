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
    start_col = row.find('S') # find returns -1 if it doesnt find what you asked in this case 'S'
    if start_col!= -1:
      startPosition = [i, start_col]
  factoryMap.append(list(row))
  conceptualmap[::-1]*y
  
for i in range(x-1):
  for j in range(y-1):
    #if factoryMap[i][j] == "C" then check up/down/left/right in factoryMap update factory map spot to *
    if factoryMap[i][j] == "C":
      factoryMap[i][j+1] = "*"
      factoryMap[i][j-1] = "*"
        
        
        
        
print(factoryMap)        

#for row
#    for col
#        while 
            #if cam *
#              check up/dpwn/left/right update factory map spot to *
  #queue startPosition
  #conceptualmap[startx][starty] = 0
#BFS


