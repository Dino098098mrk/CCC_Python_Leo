default_val = 1691600

x = int(input())
numbers = []

counter = 0

for i in range(x):
  y = input()
  numbers.append(y)
offer = input()

for i in numbers:
  if i == "1":
    default_val = default_val -100
    counter += 1
  elif i == "2":
    default_val = default_val - 500
    counter += 1
  elif i == "3":
    default_val = default_val - 1000
    counter += 1
  elif i == "4":
    default_val = default_val - 5000
    counter += 1
  elif i == "5":
    default_val = default_val - 10000
    counter += 1
  elif i == "6":
    default_val = default_val -25000
    counter += 1
  elif i == "7":
    default_val =default_val -50000
    counter += 1
  elif i == "8":
    default_val = default_val - 100000
    counter += 1
  elif i == "9":
    default_val = default_val - 500000
    counter += 1
  elif i == "10":
    default_val =default_val - 1000000
    counter += 1

if int(offer) > default_val/counter:
  print("deal")
elif int(offer) < default_val/counter:
  print("no deal")