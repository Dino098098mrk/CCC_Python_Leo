from 
array = [[0 for x in range(8)]for x in range(8)] 
constraint = [0]*8

array[1][7] = 1
array[1][4] = 1
array[2][1] = 1
array[3][4] = 1
array[3][5] = 1

print(array)


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
      
        

