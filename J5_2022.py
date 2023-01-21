numberOfGrid = int(input())
treeCount = int(input())
treeList = []

for i in range(treeCount):
  treeCord = input()  #4,7
  treeCord = treeCord.split(' ')
  xPos = int(treeCord[0])
  yPos = int(treeCord[1])
  treeList.append([xPos, yPos])

treeList.append([0, 0])
treeCount += 1
print(treeList)

extremeSize = 1000000000

largestSize = 0

totalTrees = treeCount
for i in range(totalTrees):
  for j in range(totalTrees):
    if i==j and i != treeCount-1:
      continue
    verticalBound = treeList[i][0]
    horizontalBound = treeList[j][1]
    currentSize = extremeSize
    for k in range(totalTrees):
      if k ==i or k==j:
        continue
      if treeList[k][0]>verticalBound and treeList[k][1]>horizontalBound:
        verticalWindowSize = treeList[k][0] - verticalBound - 1
        horizontalWindowSize = treeList[k][1] - horizontalBound-1
        currentSize = min(currentSize, max(verticalWindowSize, horizontalWindowSize))
      if(min(numberOfGrid-verticalBound, numberOfGrid-horizontalBound-1)<currentSize):
        currentSize = min(numberOfGrid-verticalBound, numberOfGrid-horizontalBound-1)