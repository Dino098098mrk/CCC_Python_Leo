number = 0
run = int(input())
for i in range(run):
  x = int(input())
  y = int(input())
  if x* 5 + y *3 > 40:
    number+= 1


output = str(number) + "+"

print(output)