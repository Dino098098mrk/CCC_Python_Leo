def f(n):
  counter = 1
  runtime = 0
  output = ""
  for element in range(len(n)):
    runtime += 1
    if runtime == len(n):
      output += str(counter) + " "+ n[element] + " "
      break
    if n[element] == n[element+1]:
      counter+= 1
    else:
      output += str(counter)+" "+ n[element] + " "
      counter = 1
  return output

run = int(input())

output  =[]
for i in range(run):
  n = input()
  output.append(f(n))

for i in output:
  print(i)


        
    