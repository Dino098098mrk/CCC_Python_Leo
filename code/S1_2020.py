records = []
speeds = []
times = int(input())

for i in range(times):
  timeAndLocation = str(input()).split(sep=" ")
  records.append((timeAndLocation[0],timeAndLocation[1]))
records.sort()

currentspeed, prevTime = 0,0
for i in range(len(records)):
  if i == len(records) - 1:
    break
  time, speed =  records[i][0],  records[i][1]
  if time ==0:
    currentspeed = speed
  else:
    top = abs(speed -currentspeed)
    bottom = abs(time - prevTime)
    aveSpeed = (top/bottom)
    speeds.append(aveSpeed)
# you have to test every single possible combination 


# for i in records:
#   for j in records[1:]:
#     if i[0] == j[0] and i[1] == j[1]:
#       continue
#     else:
      
#       speeds.append(abs( int(i[1])  - int( j[1]))/ abs(int(i[0]) - int(j[0])))
    
print("%.1f" % max(speeds))

# print(max(speeds))
  # get speed 

  # |X − C|/C
  
# print("%.1f",max(speeds))
