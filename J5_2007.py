distance  =[1, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
ways = [0]*7000
min = int(input())
max = int(input())
add = int(input())
# if add != 0:
#   stop = int(input())
# else:
ways = 0

for i in range(add):
  hotel= int(input())
  distance.append(hotel)
  distance.sort()


for x in distance:
  x -= 1
  if x + max >= 7000:
    for i in range(min,7000 -x):