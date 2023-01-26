number = int(input())

real = [1,2,0,0]
loops = int(number/ 1440)

def roundoff(number):
  if number >=1440:
    number = number - int(1440 * int(number/ 1440))
    return number
  else:
    return number



def addnumber(number,real):
  counter = 0
  for i in range(number):
    real[3] += 1
    if real[3] == 10:
      real[3] = 0
      real[2] += 1
    if real[2] == 6:
      real[2] = 0
      real[1] += 1
    if real[1] == 10 and real[0] != 1:
        real[1] = 0
        real[0] += 1
    if real[0] == 1 and real[1] == 3:
        real[0] = 0
        real[1] += 1

    tie = real[0] - real[1]
    if(tie== real[1]-real[2]  and tie== real[2] - real[3]):
      counter += 1

  return counter

new = roundoff(number)

result = (addnumber(new,real)

print(result)
