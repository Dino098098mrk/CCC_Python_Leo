output = ""
while(True):
  last = 
  instruction =input()

  if int(instruction) == 99999:
    break
  else:
    if (int(instruction[0]) + int(instruction[1])) % 2 == 0:
      output += "right"
    