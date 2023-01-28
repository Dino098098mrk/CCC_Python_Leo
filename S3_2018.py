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
  conceptualmap.append([-1]*y)
  
for i in range(x):
  for j in range(y):
    if factoryMap[i][j]=='C':
      #check down
      count = 0
      while True:
        if factoryMap[i+count][j] in ['.','S']:
          factoryMap[i+count][j] = '*'
        elif factoryMap[i+count][j]=='W':
          break
        count+=1

      #check up
      count = 0
      while True:
        if factoryMap[i-count][j] in ['.','S']:
          factoryMap[i-count][j] = '*'
        elif factoryMap[i-count][j]=='W':
          break
        count+=1

      #check right
      count = 0
      while True:
        if factoryMap[i][j+count] in ['.','S']:
          factoryMap[i][j+count] = '*'
        elif factoryMap[i][j+count]=='W':
          break
        count+=1

      #check left
      count = 0
      while True:
        if factoryMap[i][j-count] in ['.','S']:
          factoryMap[i][j-count] = '*'
        elif factoryMap[i][j-count]=='W':
          break
        count+=1

    
    
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


