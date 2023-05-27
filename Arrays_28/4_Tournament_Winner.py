# SOLUTION 1:
# O(n) space | O(k) space
# n = no of competitons
# k = no of teams
def tournamentWinnerSolution1(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam : 0}

    for idx,competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == 1 else awayTeam
        updateScores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3
# #############################################################

# SOLUTION 2:
def tournamentWinnerSOlution2(competitions, results):
    scores = dict()
    for idx,competition in enumerate(competitions):
        if results[idx] == 1:
            winningTeam = competition[0]
            if scores.get(winningTeam) != None:
                scores[winningTeam] = scores[winningTeam] + 3
            else:
                scores[winningTeam] = 3
        else:
            winningTeam = competition[1]
            if scores.get(winningTeam) != None:
                scores[winningTeam] = scores[winningTeam] + 3
            else:
                scores[winningTeam] = 3
    bestTeam = max(scores, key=scores.get)
    return bestTeam