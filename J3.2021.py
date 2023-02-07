output = ""
while(True):
  last = ""
  instruction =input()

  if int(instruction) == 99999:
    break
  else:
    if (int(instruction[0]) + int(instruction[1])) % 2 == 0:
      output += "right " + instruction[2:] 
      last = "right "
    elif (int(instruction[0]) + int(instruction[1])) % 2 != 0:
      output += "left " + instruction[2:] 
      last = "left "
    elif (int(instruction[0]) + int(instruction[1])) == 0:
      output += last + instruction[2:] 

    
    