distance  =[0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

min = int(input())
max = int(input())
add = int(input())
# if add != 0:
#   stop = int(input())
# else:

for i in range(add):
  hotel= int(input())
  distance.append(hotel)
  distance.sort()
  
ways = 0

if max < distance[1]:
  ways = 0

