from random import randint

def gen_index(states, n, m):
    # Randomly picks one value out of an nxm array of indices,
    # then outputs the coordinates of the picked index.
    counter= 0
    indices = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if states[i][j] == False:
                counter += 1
                indices[i][j] = counter
            else:
                indices[i][j] = 0

    r = randint(1,counter)
    
    for i in range(n):
        for j in range(m):
            if indices[i][j] == r:
                a = i
                b = j
    
    return(a, b)

def make_move(states, a, b):
    # Makes a move on the board with coordinates a, b
    states[a][b] = 1
    
    return(states)




def check_win(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        victory = "rook"
    elif abs(x2 - x1) == abs(y2 - y1):
        victory = "bishop"
    else:
        victory = "tie"
    
    return(victory)

n = 8
m = 8
rook_wins = 0
bishop_wins = 0
games = 100

for l in range(games):
    
    board = [[0 for j in range(m)] for i in range(n)]
    
    #playing a game
    x1, y1 = gen_index(board, n, m)
    board = make_move(board, x1, y1)

    x2, y2 = gen_index(board, n, m)
    board = make_move(board, x2, y2)

    winner = check_win(x1, y1, x2, y2)
    
    if winner == "rook":
        rook_wins += 1
    elif winner == "bishop":
        bishop_wins += 1

print("Rook won " + str(rook_wins) + " times")
print("Bishop won " + str(bishop_wins) + " times")