arr = []
new = []
while(True):
  first = str(input())
  second = str(input())
  arr.append([first,second])
  if second == "SCHOOL":
    break

for i in range(len(arr)-1,-1,-1):
  if arr[i][1] == arr[0][1]:
    new.append([arr[i][0],"HOME"])
  else:
    new.append([arr[i][0],arr[i-1][1]])

for i in new:
  if i[0] == "R":
    i[0] = "LEFT"
  else:
    i[0] ="RIGHT"

  if i[1] != "HOME":
    print("Turn "+ i[0] + " onto "+ i[1]+ " street.")
  else:
    print("Turn "+ i[0] + " into your HOME.")
  
  
#compeleted 
