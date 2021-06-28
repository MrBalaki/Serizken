import sqlite3
from collections import namedtuple
from serizken_data import G_rf, G_lf, rt, lt

GameEval = namedtuple('GameEval', ['score', 'path'])

max_depth = 10

con = sqlite3.connect('serizken.db')
cur = con.cursor()
cur.execute("SELECT node, distance_lt, distance_rt FROM Distances JOIN Nodes ON Nodes.node_ID = Distances.node_ID")
result = cur.fetchall()
dists = {tuple(map(int, item[0][1:-1].split(', '))):(item[1], item[2]) for item in result}
con.close()


def minimax(node, alpha=float('-inf'), beta=float('inf'), is_maximizing=True, depth=0) -> GameEval:
    if node in lt:
        return GameEval(score=float('inf'), path=[])
    if node in rt:
        return GameEval(score=float('-inf'), path=[])
    
    if depth >= max_depth:
        return GameEval(score=dists[node][1] - dists[node][0], path=[])
    
    if is_maximizing:
        #print("--+--")
        best_score = float('-inf')
        best_path = []
        branches = G_lf[node]
    
        for branch in branches:
            evalution = minimax(branch, alpha, beta, False, depth+1)

            if best_score <= evalution.score:
                if len(evalution.path) < 2:
                    best_score = evalution.score
                    best_path = evalution.path.copy()
                    best_path.append(branch)
                elif branch != evalution.path[-2]:
                    best_score = evalution.score
                    best_path = evalution.path.copy()
                    best_path.append(branch)
                
                if best_score >= beta:
                    break
            
            alpha = max(alpha, best_score)
        
        return GameEval(score=best_score, path=best_path)
    else:
        best_score = float('inf')
        best_path = []
        branches = G_rf[node]
        for branch in branches:
            evalution = minimax(branch, alpha, beta, True, depth+1)

            if best_score >= evalution.score:
                if len(evalution.path) < 2:
                    best_score = evalution.score
                    best_path = evalution.path.copy()
                    best_path.append(branch)
                elif branch != evalution.path[-2]:
                    best_score = evalution.score
                    best_path = evalution.path.copy()
                    best_path.append(branch)

                if best_score <= alpha:
                    break
            
            beta = min(beta, best_score)
            
        return GameEval(score=best_score, path=best_path)