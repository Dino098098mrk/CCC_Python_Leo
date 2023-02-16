#recursion
def isCrystal(magLevel, x,y):
  if magLevel == 1:
    if (x,y) in {(1,0),(2,0),(3,0),(2,1)}:
      return True
    else:
      return False

  zoomout_x = x 
  zoomout_y = y
  
  for i in range(magLevel-1): # looping divided by 5 each time beacuse maginfies goes up by 5 each time
    zoomout_x //= 5 # going to the lowest level 
    zoomout_y //= 5 # going to the lowest level 2.4->2;  5.9->5

  #after going to the lowest level you check
  if(zoomout_x, zoomout_y) in {(1,0),(2,0),(3,0),(2,1)}:
    return True
    
  elif(zoomout_x, zoomout_y) in {(1,1),(2,2),(3,1)}: # according to the question if the x and y posistion is right above the default cyrstals you need to check it.
    return isCrystal(magLevel-1,x%(5**(magLevel-1)),y%(5**(magLevel-1))) #x%(5**(magLevel-1)
  else: 
    return False
  
    
CountT = int(input())
testCases = []
for i in range(CountT): #take away: map()
 testCases.append(list(map(int,input().split()))) # adds value to the list 
for case in testCases:
  if isCrystal(case[0], case[1], case[2]):
    print("crystal")
  else:
    print("empty")

