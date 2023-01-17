#recursion problem
def monkeyAword(x):
  if x == 'A':
    return True
  if len(x)>=3 and x[0] == 'B' and x[-1]=='S' and monkeyWord(x[1:len(x)-1]):
    return True
  return False

def monkeyWord(x):
  if monkeyAword(x):
    return True
  for i in range(1,len(x)):
    if x[i] == 'N' and monkeyAword(x[:i]) and monkeyWord(x[i+1:]):
      return True
  return False

while True:
  x = input()
  if x == 'X':
    break
  if monkeyWord(x):
    print("YES")
  else:
    print("NO")





  