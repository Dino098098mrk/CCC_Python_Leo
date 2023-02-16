Jerseys =int(input())
Athlete = int(input())
size = []
goal = []

numberused = []
counter = 0
for i in range(Jerseys):
  theSize = str(input())
  size.append(theSize)

for i in range(Athlete):
  want = str(input()).split(" ")
  goal.append(want)


for i in goal:
  if i[0] in size:
    if i[1] not in numberused:
      numberused.append(i[1])
      size.remove(i[0])
      counter += 1

print(counter)
