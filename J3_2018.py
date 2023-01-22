def first(list):
  output = ""
  counter = 0
  for i in list:
    counter += int(i)
    output += str(counter) + " "

  return output
    
def second(list):
  list1 = first(list).split( )
  output = ""
  prime = list1[1]
  for i in list1:
    if i == 0:
      output+= str(prime) + " "
    else:
      output += str(abs(int(prime) - int(i))) + " "

  return output
  
def third(list):
  list1 = first(list).split( )
  output = ""
  prime = list1[2]

  for i in list1:
    if i == 0:
      output+= str(prime) + " "
    else:
      output += str(abs(int(prime) - int(i))) + " "
  return output 


def fourth(list):
  list1 = first(list).split( )
  output = ""
  prime = list1[3]

  for i in list1:
    if i == 0:
      output+= str(prime) + " "
    else:
      output += str(abs(int(prime) - int(i))) + " "
  return output 

def fifth(list):
  list1 = first(list).split( )
  output = ""
  prime = list1[4]

  for i in list1:
    if i == 0:
      output+= str(prime) + " "
    else:
      output += str(abs(int(prime) - int(i))) + " "
  return output 

x = input().split()
list = [0,]
for i in x:
  list.append(i)


print(first(list))
print(second(list))
print(third(list))
print(fourth(list))
print(fifth(list))



  