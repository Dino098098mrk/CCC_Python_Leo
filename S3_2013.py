print("23/02/04")
#teams: 1,2,3,4
game_list = [[1,2],[2,3],[1,3],[2,4],[4,1],[3,4]]

favteam = int(input())
gameplayed = int(input())

for i in range(gameplayed):
  game_result = input().split()
  team1 = int(game_result[0])
  team2 = int(game_result[1])
  t1Score = int(game_result[2])
  t2Score = int(game_result[3])


