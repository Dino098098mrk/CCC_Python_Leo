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
    
print(max(speeds))
  # get speed 

  # |X − C|/C
  
# print("%.1f",max(speeds))
