x = int(input("Enter m: "))
y = int(input("Enter n: "))

counter = 0


for i in range(1,x+1):
  for j in range(1,y+1):
    if i + j == 10:
      counter += 1

print(counter)
# CCC solution 2006