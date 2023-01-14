
#a dictionary for storing every keys
key_map = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777",
    "s": "7777", "t": "8", "u": "88",
    "v": "888", "w": "9", "x": "99",
    "y": "999", "z": "9999"
}

word = str(input())
count = 0
prev = ""

for i in word:
  if prev == key_map[i][0]:
    count += 2
  count += len(key_map[i])
  prev = key_map[i][0]

print(count)
  