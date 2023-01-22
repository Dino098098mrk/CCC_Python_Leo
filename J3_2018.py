def first(list):
  output = ""
  counter = 0
  for i in list:
    counter += i
    output += counter + " "
    
    

x = input().split()
list = [0,]
for i in x:
  list.append(i)
print(first(list))




  