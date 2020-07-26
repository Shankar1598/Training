def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print()

def isSafe(board, row, col):
  safe = True
  for lc in range(col):
    if board[row][lc] == 1:
      safe = False

  # Check upper diagonal on left side 
  diagonal1 = zip(range(row, -1, -1), range(col, -1, -1))
  for i, j in diagonal1:
    # print(list(diagonal1))
    if board[i][j] == 1: 
      return False

  # Check lower diagonal on left side 
  diagonal2 = zip(range(row, N, 1), range(col, -1, -1))
  for i, j in diagonal2:
    # print(list(diagonal2))
    if board[i][j] == 1: 
      return False

  # print("safe: " + str(safe))
  return safe

def solveNQ(board, col):
  global N
  
  if col >= N:
    return True

  for row in range(N):
    if isSafe(board, row, col):
      board[row][col] = 1

      if solveNQ(board, col + 1):
        return True
      board[row][col] = 0
      
  return False


N = 5
board = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

if solveNQ(board, 0):
  printSolution(board)
else:
  print("Solution not found")