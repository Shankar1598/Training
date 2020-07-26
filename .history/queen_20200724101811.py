

def solveNQ(board, col):

  if col >= N:
    return True

  for row in range(N):
    if isSafe(board, row, col):
      board[row][col] = 1

      if solveNQ(board, col + 1):
        return True
      
      board[row][col] = 0
    



board = [
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]
N = len(board)