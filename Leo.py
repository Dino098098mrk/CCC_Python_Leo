#15/15 Good
def J1():
  x = int(input())
  y = int(input())
  z = int(input())

  result = 0

  biggest = max(x, y, z)
  smallest = min(x, y, z)

  if x != biggest and x != smallest:
    result = x
  elif y != biggest and y != smallest:
    result = y
  else:
    result = z
  print(result)


# J1()


#should be 15/15, make sure your output is consistent with the question
#CCC rule: Output must match the output format specified in the problem exactly. Prompts or additional output must not be produced.
def J2():
  # lower = int(input("Enter lower limit of range"))
  # high = int(input("Enter higher limit of range"))
  lower = int(input())
  high = int(input())

  num = 0

  def divisor(n):
    l = []
    for i in range(1, n + 1):
      if (n % i == 0):
        l.append(i)
    return l

  for i in range(lower, high + 1):
    if (len(divisor(i)) == 4):
      num += 1
  print(num)
  # print(f"The number of RSA numbers between {lower} and {upper} is {counter}")


# J2()


#3/15
#output should match the output format
#logic error
def J3():
  #changed below
  input_taken = int(input())

  first = int(input())

  second = int(input())

  third = int(input())

  list = [first, second, third]
  track = 0
  counter = 0

  while (input_taken > 0):
    list[track] = list[track] + 1
    counter += 1

    if track == 0 and list[track] == 35:
      input_taken -= 30
      list[track] = 0
    if track == 1 and list[track] == 100:
      input_taken -= 60
      list[track] = 0
    if track == 2 and list[track] == 10:
      input_taken -= 9
      list[track] = 0

    if track == 2:
      track = 0
  print("Martha plays " + str(counter - 1) + " times before going broke.")


# J3()

#format not correct, should be integers (input 28 & 7)
#3.33/15
import math


def J4():
  #changed below
  numerator = int(input())
  denominator = int(input())

  counter = 0

  if (numerator % denominator == 0):
    print((int)(numerator / denominator))  #has been changed

  elif (numerator == 0 or denominator == 0):
    print(0)

  else:
    while (numerator > denominator):
      numerator -= denominator
      counter += 1

    if (math.gcd(numerator, denominator) != 1):
      print(
        str(int(counter)) + " " +
        str(int(numerator / math.gcd(numerator, denominator))) + "/" +
        str(int(denominator / math.gcd(numerator, denominator))))
    else:
      print(str(int(counter)) + " " + str(numerator) + "/" + str(denominator))


# J4()


def J5():
  pass


# J5()
