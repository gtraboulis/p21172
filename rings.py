from random import randint

def gen_index(states, n):
    # Randomly picks one value out of an nxnxn array of indices,
    # then outputs the coordinates of the picked index.
    counter= 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if states[i][j][k] == True:
                    counter = counter + 1
                    indices[i][j][k] = counter
                else:
                    indices[i][j][k] = 0

    r = randint(1,counter)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if indices[i][j][k] == r:
                    a = i
                    b = j
                    c = k
    
    return(r, a, b, c)

def make_move(states, a, b, c, moves):
    # Makes a move on the board with coordinates a, b, c and increments moves counter
    states[a][b][c] = 0
    moves = moves + 1
    
    return(states, moves)

def check_win(states, a, b, c):
    # Checking for victory. This is done using the coordinates of the latest move
    # to improve efficiency 
    if (states[a][b][0] == states[a][b][1] == states[a][b][2] == False #Horizontally, same size
    or states[a][0][c] == states[a][1][c] == states[a][2][c] == False #Vertically, same size
    or states[a][0][0] == states[a][1][1] == states[a][2][2] == False #Top left to bottom right, same size
    or states[a][0][2] == states[a][1][1] == states[a][2][0] == False #Top right to bottom left, same size
    or states[0][b][0] == states[1][b][1] == states[2][b][2] == False #Horizontally, increasing size
    or states[2][b][0] == states[1][b][1] == states[0][b][2] == False #Horizontally, decreasing size
    or states[0][0][c] == states[1][1][c] == states[2][2][c] == False #Vertically, increasing size
    or states[2][0][c] == states[1][1][c] == states[0][2][c] == False #Vertically, decreasing size
    or states[0][0][0] == states[1][1][1] == states[2][2][2] == False #Top left to bottom right, increasing size
    or states[2][0][0] == states[1][1][1] == states[0][2][2] == False #Top left to bottom right, decreasing size
    or states[0][0][2] == states[1][1][1] == states[2][2][0] == False #Top right to bottom left, increasing size
    or states[2][0][2] == states[1][1][1] == states[0][2][0] == False): #Top right to bottom left, decreasing size
        victory = True
    else:
        victory = False
    
    return(victory)


n=3 # Dimensions of board and possible ring sizes
movessum = 0
iterations = 100000

for l in range(iterations):
    
    # Reinitializing after every loop
    states = [[[1 for k in range(n)] for j in range(n)] for i in range(n)] # Empty board
    indices = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    victory = False
    moves = 0
    
    
    while victory == False:
        
        r, a, b, c = gen_index(states, n)
        states, moves = make_move(states, a, b, c, moves)
        victory = check_win(states, a, b, c)
        
    movessum = movessum + moves

avgmoves = movessum/iterations
print(avgmoves)   