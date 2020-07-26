class Maze:

  def print(self, maze):
    for row in range(self.N):
      for col in range(self.N):
        print(str(maze[row][col]), end= "")
      print()

  def solve(self, maze):
    self.maze = maze
    self.N = len(maze)

    solution = [[ 0 for j in range(self.N)] for i in range(self.N)]

    if self.solveMaze(0, 0, solution):
      self.print(solution)

  def solveMaze(self, x, y, sol):
    N  = self.N