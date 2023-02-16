run = int(input())

letter={'A':2, 'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}

#for aletter in anInput
  # if aletter in letter.keys()
  #    output+= letter[aletter]
output = ""
counter =0
for i in range(run):
  phoneNumber = str(input()).replace("-","") # replace something to something
  for index in range(len(phoneNumber)):
    if phoneNumber[index] in letter.keys():
      output+= str(letter[phoneNumber[index]])
    else:
      output+=phoneNumber[index]
    if(counter==2 or counter == 5):
      output+='-'
    counter+=1
  output+= "\n"
  counter = 0
  



print(output)