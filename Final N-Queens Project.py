a="""This is a program used to display ALL solutions for the famous N-Queens Problem
in chess. The N-Queens Problem is a problem where in an N-sized chess board, we have
to place N Queens in such a way that no one queen can attack any other queen"""
print(a)
print()
a="""This program will take your input and will generate the solutions for the board 
size of your input"""

#This function generates an nxn board as a matrix
def generateboard(n):
    try:
        n=int(n)
        board=[[0]*n for i in range(n)]
        return board
    except Exception as e:
        print("The following error has occured:",e)

#This function displays the solution
def FinalSolution(board):
    for i in board:
        for j in i:
            if j:
                print('Q',end=' ')
            else:
                print('.',end=' ')
        print()
    print()

#This is the main algorithm of the program, and determines whether a queen can 
#be placed in a particular box or not. It considers a particular location in 
#a chessboard and sees if another queen can attack the location under 
#consideration.
def safe(board,row,col):
    #TO CHECK IF THE CURRENT ROW IS SAFE
    c=len(board)
    for i in board[row]:
        if i:
            return 0
        
    #TO CHECK IF THE CURRENT COLUMN IS SAFE
    for i in range(len(board)):
        if board[i][col]:
            return 0
        
    a,b=row,col
    #TO CHECK IN THE BOTTOM-RIGHT DIRECTION
    while a<c and b<c:
        if board[a][b]:
            return 0
        a=a+1
        b=b+1
        
    a,b=row,col
    #TO CHECK IN THE TOP-LEFT DIRECTION
    while a>=0 and b>=0:
        if board[a][b]:
            return 0
        a=a-1
        b=b-1
    a,b=row,col
    #TO CHECK IN THE TOP-RIGHT DIRECTION
    while a>=0 and b<c:
        if board[a][b]:
            return 0
        a=a-1
        b=b+1
    a,b=row,col
    #TO CHECK IN THE BOTTOM-LEFT DIRECTION
    while a<c and b>=0:
        if board[a][b]:
            return 0
        a=a+1
        b=b-1
    return 1

#This function takes the generated board, and tries all possible combinations
#of queens. It places the queens in all locations to see which is the correct
#overall solution. The best part about this function is that it if it sees that
#N-queens cannot be placed, it does not restart but instead continues from the 
#last value. 
Number=0
def solve(board,row=0):
    if board != None:    
        global Number
        if row>=len(board):
            FinalSolution(board)
            Number+=1
            return       
    
        for col in range(len(board)):
            if safe(board,row,col):
                board[row][col]=1
                solve(board,row+1)#The board is returned here when a solution 
                #is found and the program is out of the function.
                board[row][col]=0

        
n=input("Enter the size 'n' of the board:")
a=generateboard(n)
solve(a)
print("The number of solutions for the",n,"x",n,"board is:", Number)