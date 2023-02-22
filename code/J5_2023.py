word = str(input())

down = int(input())
straight = int(input())

map = []
for z in range(down):
  map.append([])

for i in range(len(map)):
  inp = str(input())
  for j in range(len(inp)):
    if inp[j] == ' ':
      continue
    else:
      map[i].append(inp[j])

print(map)


def horiz(map):
  count = 0
  result = 0

  empty = ""
  for line in map:
    for letter in line:
      if letter == word[count]:
        empty += word[count]
        count += 1
      else:
        count = 0
        continue
    if empty == word:
      result += 1

    count = 0
    empty = ""
  return result


def horiz_reverse(map):
  count = 0
  result = 0

  empty = ""
  for line in map:
    for letter in line[::-1]:
      if letter == word[count]:
        empty += word[count]
        count += 1
      else:
        count = 0
        continue
    if empty == word:
      result += 1

    count = 0
    empty = ""
  return result


final = 0
final = final + horiz(map)
final = final + horiz_reverse(map)

print(final)
