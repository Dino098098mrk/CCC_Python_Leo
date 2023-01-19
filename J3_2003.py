total = 1
while(True):
  print("Enter sum of dice:")
  x = int(input(""))
  if x == 0:
      print("You Quit!")
      break
  total += x
  if total == 54:
    total = 19
  if total == 90:
    total = 48
  if total == 99:
    total = 77
  if total == 9:
    total =34
  if total == 40:
    total = 64
  if total == 67:
    total =86
    
  print("You are now on square " + str (total))
  if total == 100:
    print("You Win!")
    break
  