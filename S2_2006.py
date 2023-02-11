plaintext = str(input())
encrypted = str(input())
translate = str(input())
dict =dict()
for i in range(len(plaintext)):
  if(encrypted[i] not in dict.keys):
    dict[encrypted[i]]=plaintext[i]


