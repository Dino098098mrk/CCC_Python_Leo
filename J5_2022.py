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
    