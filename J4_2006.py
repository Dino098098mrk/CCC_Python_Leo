from queue import PriorityQueue
array = [[0 for x in range(8)]for x in range(8)] 
constraint = [0]*8

array[1][7] = 1
array[1][4] = 1
array[2][1] = 1
array[3][4] = 1
array[3][5] = 1

# print(array)


while(True):
  x = int(input())
  y = int(input())
  if x == 0 and y == 0:
    break
  else:
    array[x][y] = 1


for i in array:
    for j in range(1,8):
      if i[j] ==  1:
        constraint[j] +=1

print(constraint)

pq = PriorityQueue() #min heap
output = []
for i in range(1,8):
  if constraint[i] == 0:
    pq.put(i)

while not pq.empty():
  task =pq.get()
  output.append(task)
  for i in range(1,8):
    if array[task][i]==1:
      constraint[i] -=1
      if constraint[i]==0:
        pq.put(i)
        
        

