def isSafe(board, row, col):
  for lc in range(col):
    if board[row][lc] == 1:
      return False

  leftTop = zip(range(row, -1, -1), range(col, -1, -1))
  for lr, lc in leftTop:
    print("Checking left top:", end=" ")
    print(list(leftTop))
    if board[lr][lc] == 1:
      return False

  leftBot = zip(range(row, N, 1), range(col, -1, -1))
  for lr, lc in leftBot:
    if board[lr][lc] == 1:
      return False

  return True

def solveNQ(board, col):
  if col >= N:
    return True

  for row in range(N):
    if isSafe(board, row, col):
      board[row][col] = 1

      if solveNQ(board, col + 1):
        return True
      
      board[row][col] = 0
    
    return False

def printBoard(board):
  for i in range(N):
    for j in range(N):
      print(str(board[i][j]), end= " ")
    print()


board = [
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]
N = len(board)

res = solveNQ(board, 0)
if res:
  printBoard(board)
else:
  print("Solution not found")