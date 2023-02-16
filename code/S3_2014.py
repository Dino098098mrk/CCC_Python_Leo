times = int(input())
queue = []
stack = [9999]
result = True
output = ""
for i in range(times):
  length = int(input())
  min = 1
  for i in range(length):
    item = int(input())
    queue.append(item)
  queue.reverse()
  for c in range(0, len(queue), 1):
    if min == queue[c]:
      min+=1
    elif(queue[c] > stack[-1]):
      result = False
      break
    else:
      stack.append(queue[c])
  if result == False:
    output += "N" + " "
  else:
    output += "Y" + " "

      
    #if min == next cart
    #  contitnue
    #else if min ! = nextcart and min < stack[-1]
      #stack.append(nextcart)
    #else:
      #print no
  print(output)
    