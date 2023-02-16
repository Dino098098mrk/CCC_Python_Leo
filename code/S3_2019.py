def findSingleX(x,y,z):
  if x =='X':
    x = y+y-z
  elif y == "X":
    y = (x+z)//2
  else: 
    z = y + (y-x)
  return x,y,z

def findMultipleX(x,y,z):
  if x == "X" and y =="X" and z =="X":
    x = 0
    y = 2
  elif x ==y =='X':
    y = z+2
    x = z+4
  elif y== z=="X":
    y = x+2
    z = x+4
  elif x == z=="X":
    x = y-2
    z = y+2
  return x,y,z
  


  
asquare=[0]*9
for i in range(3):
  line = input()
  line = line.split()
  for j in range(3):
    if line[j] == 'X':
      asquare[i*3+j]='X'
    else:
      asquare[i*3+j]= int(line[j])

while True:
  multipleX = True
  for i in range(3):
    if [asquare[i*3], asquare[i*3+1], asquare[i*3+2]].count('X') == 1:
      multipleX = False
      asquare[i*3], asquare[i*3+1], asquare[i*3+2] = findSingleX(asquare[i*3], asquare[i*3+1], asquare[i*3+2])
  for i in range(3):
    if [asquare[i], asquare[i+3], asquare[i+6]].count('X') == 1:
      multipleX = False
      asquare[i], asquare[i+3], asquare[i+6] = findSingleX(asquare[i], asquare[i+3], asquare[i+6])
  if asquare.count('X') == 0:
    break
  if multipleX:
      for i in range(3):
        if [asquare[i*3], asquare[i*3+1], asquare[i*3+2]].count('X') > 1:
          asquare[i*3], asquare[i*3+1], asquare[i*3+2] = findMultipleX(asquare[i*3], asquare[i*3+1], asquare[i*3+2])
      for i in range(3):
        if [asquare[i], asquare[i+3], asquare[i+6]].count('X') > 1:
          asquare[i], asquare[i+3], asquare[i+6] = findMultipleX(asquare[i], asquare[i+3], asquare[i+6])
      
 #print the final  

for i in range(3):
  print(asquare[i*3], asquare[i*3+1], asquare[i*3+2])
  
      