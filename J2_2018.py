user_input = int(input())
list1 =input()
list2 = input()

result = 0

for i in range(user_input):
  if list1[i] == "C" and list2[i] == "C":
    result += 1
    
print(result)
  