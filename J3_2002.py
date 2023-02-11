from itertools import combinations
#posiblilty
pink = int(input("Cost of PINK tickets:")) 
green = int(input("Cost of GREEN tickets:")) 
red = int(input("Cost of RED tickets:"))
orange = int(input("Cost of ORANGE tickets:"))
limit = int(input("How much must be raised with ticket sales?")) 

counter = 0
o = 0
r = 0
g = 0
p = 0
while o<100:
  r=0
  while r<100:
    g=0
    while g<100:
      p=0
      while p<100:
        if(p*pink+green*g+red*r+orange*o) == limit:
          print("pink: ", p, " green ", g, " red ", r," orange ",o)
          counter+=1
          break
        p+=1
      g+=1
    r+=1
  o+=1
print(counter)