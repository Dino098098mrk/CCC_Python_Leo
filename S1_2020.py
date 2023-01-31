records = []
speeds = []

times = int(input())

for i in range(times):
  timeAndLocation = str(input()).split(sep=" ")
  records.append((timeAndLocation[0],timeAndLocation[1]))
records.sort()


for i in range(len(records)):
  if i == len(records) - 1:
    break
  else:
    top = abs(int(records[i][1]) -int(records[i+1][1]))
    bottom = abs(int(records[i][0]) - int(records[i+1][0]))
    speeds.append((top/bottom))
# you have to test every single possible combination 


for i in records:
  for j in records[1:]:
    if i[0] == j[0] and i[1] == j[1]:
      continue
    else:
      
      speeds.append(abs( int(i[1])  - int( j[1]))/ abs(int(i[0]) - int(j[0])))
    
print(max(speeds))

# print(max(speeds))
  # get speed 

  # |X − C|/C
  
# print("%.1f",max(speeds))
