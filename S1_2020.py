records = []
speeds = []


times = int(input())

for i in range(times):
  Input = str(input())
  timeAndLocation = Input.split()
  timeAndLocation = map(int,timeAndLocation)