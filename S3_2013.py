def bruteForce():
  def predict(predictSize,level,match):
    size = predictSize
    for i in range(level):
      size /=3
    size = int(size)
    for possibility in range(pow(3, level-1)):
      for i in range(size*(possibility*3),size*(possibility*3+1)):
        predictboard[i][match[0]-1]+=3
      for i in range(size*(possibility*3+1),size*(possibility*3+2)):
        predictboard[i][match[1]-1]+=3
      for i in range(size*(possibility*3+2),size*(possibility*3+3)):
        predictboard[i][match[0]-1]+=1
        predictboard[i][match[1]-1]+=1
  
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
  
  predictboard = [[*teamscore] for i in range(pow(3,6-gameplayed))]
  predictionlevel = 1
  
  for match in game_list:
    predict(len(predictboard), predictionlevel, match)
    predictionlevel+=1
  
  favteam-=1
  winingCount = 0
  for state in predictboard:
    favteamScore = int(state[favteam])
    state.sort()
    if favteamScore > state[2]:
      winingCount+=1
  print(winingCount)
# bruteForce()
def BFS():
  game_list = [[1,2],[2,3],[1,3],[2,4],[1,4],[3,4]]
  teamscore = {1:0, 2:0, 3:0, 4:0}
  favteam = int(input())
  gameplayed = int(input())
  for i in range(gameplayed):
    game_result = input().split()
    team1 = int(game_result[0])
    team2 = int(game_result[1])
    t1Score = int(game_result[2])
    t2Score = int(game_result[3])
    if t1Score > t2Score:
      teamscore[team1] += 3
    elif t2Score > t1Score:
      teamscore[team2] += 3
    else:
      teamscore[team1] += 1
      teamscore[team2] += 1
    game_list.remove([team1,team2])
  def breadFirstSearch(board, matchList):
    count = 0
    queue = [(board, matchList)]
    while queue:
      scoreState, nextMatch = queue.pop(0)
      if not nextMatch:
        if max(scoreState.values()) == scoreState[favteam] and list(scoreState.value()).count(max(scoreState.values()))<2:
          count+=1
        continue
      team1, team2 = nextMatch[0][0], nextMatch[0][1]
      tempResult = list(nextMatch)
      tempResult.pop(0)
      win, tie, lose = scoreState.copy(), scoreState.copy(),scoreState.copy()
      win[team1] +=3
      tie[team1] +=1
      tie[team2] +=1
      lose[team2] +=3
      queue.append((win, tempResult))
      queue.append((tie, tempResult))
      queue.append((lose, tempResult))
BFS()