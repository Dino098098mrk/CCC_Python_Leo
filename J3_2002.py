from itertools import combinations as com

pink = int(input("Cost of PINK tickets:"))
green = int(input("Cost of GREEN tickets:"))
red = int(input("Cost of RED tickets:"))
orange = int(input("Cost of ORANGE tickets:"))
limit = int(input("How much must be raised with ticket sales?"))

#write a function that takes pink, green, red and orange tickets and returns all possible combination to make limit
def ticket_combinations(pink, green, red, orange):
  return com(pink, green, red, orange)

print(ticket_combinations(pink, green, red, orange))