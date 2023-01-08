first = str(input("Enter first phrase> "))
second = str(input("Enter second phrase> "))
result = False
resultfinal = True
for i in range(len(first)):
  if first[i] in second:
    result = True
  else:
    result = False
    resultfinal = False
    break

for i in range(len(second)):
  if second[i] in first:
    result = True
  else:
    result = False
    resultfinal = False
    break



print(resultfinal)