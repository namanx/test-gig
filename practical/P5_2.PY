
colSet = set()
posDia = set() # (r + c)
negDia = set() # (r - c)

result = []

n = int(input("Enter Number Of Queens: "))

board = [[0]*n for i in range(n)]

def backtrack(row):
    if row == n:
        copy = ["".join(str(row)) for row in board]
        result.append(copy)
        return

    for col in range(n):
        if col in colSet or (row - col) in negDia or (row + col) in posDia:
            continue
        
        colSet.add(col)
        posDia.add(row + col)
        negDia.add(row - col)
        board[row][col] = 1
        
        backtrack(row + 1)
        
        colSet.remove(col)
        posDia.remove(row + col)
        negDia.remove(row - col)
        board[row][col] = 0
    
backtrack(0) 

def printSolution(result): 
    pass
    for i in result:
        for j in i:
            print(j)
        print()
        
        
printSolution(result)
    