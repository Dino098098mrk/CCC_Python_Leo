def isCrystal(magLevel, x,y):
  if magLevel == 1:
    if (x,y) in {(1,0),(2,0),(3,0),(2,1)}:
      return True
    else:
      return False

  zoomout_x = x 
  zoomout_y = y
  for i in range(magLevel-1):
    zoomout_x //= 5
    zoomout_y //= 5
  if(zoomout_x, zoomout_y) in {(1,0),(2,0),(3,0),(2,1)}:
    return True
  elif(zoomout_x, zoomout_y) in {(1,1),(2,2),(3,1)}:
    return isCrystal(magLevel-1,x%(5**(magLevel-1)),y%(5**(magLevel-1)))
  
    
CountT = int(input())
testCases = []
for i in range(CountT): #take away: map()
 testCases.append(list(map(int,input().split()))) # adds value to the list 
for case in testCases:
  if isCrystal(case[0], case[1], case[2]):
    print("crystal")
  else:
    print("empty")

