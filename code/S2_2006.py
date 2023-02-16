plaintext = str(input())
encrypted = str(input())
translate = str(input())
dict =dict()

output = ""
#construct dictionary
for i in range(len(plaintext)):
  if(encrypted[i] not in dict.keys()):
    dict[encrypted[i]]=plaintext[i]

#translate
for i in translate:
  if i not in dict:
    output += '.'
  else:
    output += dict[i]


print(output)