times = int(input())
output = ""
for i in range(times):
  x = str(input()).split(sep=" ")
  run = x[0]
  symbol = x[1]

  item = ""
  for i in range(int(run)):
    item+= symbol

  output += item + "\n"
  item = ""


print(output)
  