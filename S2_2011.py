run = int(input())

answer = ""
key = ""

count = 1

for i in range(run*2):
  if count >3:
    key.append(i)
  else:
    answer.append(i)

