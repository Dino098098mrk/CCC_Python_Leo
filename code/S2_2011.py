run = int(input())
answer = []
key = []
count = 1
matches = 0

for i in range(run*2):
  x = str(input())
  if count >run:
    key.append(x)
  else:
    answer.append(x)

  count += 1

for i in range(run):
  if answer[i] == key[i]:
    matches+= 1


print(matches)

