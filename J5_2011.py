from itertools import combinations
def getCombination(k):
  totalPeople = [x for x in range(1,k+1)]
  b = []
  for howManyPeopleToKick in range(2,k+1):
    b+=list(map(list, list(combinations(totalPeople, howManyPeopleToKick))))
  return b
    



n = int(input())
friendsDict = {}
for x in range (1,n+1):
  friendsDict[x] = []
for x in range(1,n):
  friendsDict[int(input())].append(x)
allPossibleList = getCombination(n-1)
for x in range(1,n):
  allPossibleList.append([x])
allPossibleList.append([])
for combination in range(len(allPossibleList)):
  flag = True
  while flag: 
    flag = False
    for inviter in range(len(allPossibleList[combination])):
      friends=friendsDict[allPossibleList[combination][inviter]]
      for friend in friends:
        if friend not in allPossibleList[combination]:
          allPossibleList[combination]+=[friend]
          flag=True
visited = []
count = 0
for combination in allPossibleList:
  if sorted(combination) in visited:
    continue
  else:
    visited.append(sorted(combination))
    count+=1
print(count)