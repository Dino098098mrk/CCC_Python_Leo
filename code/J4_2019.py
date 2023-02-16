grid = [[1,2],[3,4]]

x = input();

#flip grid[0][0] with grid[1][0]
#flip grid[0][1] with grid[1][1]

for i in range(len(x)):
  if x[i] == "H":
    temp = grid[0][0];
    temp2 = grid[1][0];
    grid[1][0] = temp
    grid[0][0] = temp2

    temp3 = grid[0][1];
    temp4 = grid[1][1];
    grid[1][1] = temp3
    grid[0][1] = temp4

  else:
    temp = grid[0][0];
    temp2 = grid[0][1];
    grid[0][0] = temp2
    grid[0][1] = temp

    temp3 = grid[1][0];
    temp4 = grid[1][1];
    grid[1][0] = temp4
    grid[1][1] = temp3

    
print(str (grid[0][0])  + " " + str(grid[0][1]))
print(str(grid[1][0]) + " " + str(grid[1][1]))