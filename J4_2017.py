number = int(input())

real = [1,2,0,0]
loops = int(number/ 1440)

def roundoff(number):
  if number >=1440:
    number = number - int(1440 * int(number/ 1440))



roundoff(number)