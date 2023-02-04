print("23/02/04")
#teams: 1,2,3,4
game_list = [[1,2],[2,3],[1,3],[2,4],[1,4],[3,4]]
teamscore = [0,0,0,0]

favteam = int(input())
gameplayed = int(input())

for i in range(gameplayed):
  game_result = input().split()
  team1 = int(game_result[0])
  team2 = int(game_result[1])
  t1Score = int(game_result[2])
  t2Score = int(game_result[3])
  game_list.remove([team1,team2])
  if t1Score > t2Score:
    teamscore[team1-1] += 3
  elif t2Score > t1Score:
    teamscore[team2-1] += 3
  else:
    teamscore[team1-1] += 1
    teamscore[team2-1] += 1


#list(teamscore * rows)
#[teamscore]