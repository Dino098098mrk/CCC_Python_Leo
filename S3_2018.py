#1. factory
#2. conceptual map

rowcol = input().split()
x = int(rowcol[0])
y = int(rowcol[1])

startPosition = None
factorymap = []
conceptualmap = []

for i in range(x):
  row = input()
  if startPosition is None:
    start_col = row.find('S') # find returns -1 if it doesnt find what you asked in this case 'S'
    if start_col!= -1:
      startPosition = [i, start_col]
  factoryMap.append(list(row))
  conceptualmap[-1]*y