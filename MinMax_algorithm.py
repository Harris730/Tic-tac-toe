class MinMax:
    def _init_(self, GameBoard):
     self.GameBoard = GameBoard
    def evaluate(self):
    # 1 = x won
    # 0 = tie
    # -1 = o won
     for row in range(3):
       if self.GameBoard[row][0] == self.GameBoard[row][1] and self.GameBoard[row][1] == self.GameBoard[row][2]:
         if self.GameBoard[row][0] == 'x':
           return 1
         elif self.GameBoard[row][0] == 'o':
           return -1
     for col in range(3):
      if self.GameBoard[0][col] == self.GameBoard[1][col] and self.GameBoard[1][col] == self.GameBoard[2][col]:
        if self.GameBoard[0][col] == 'x':
            return 1
        elif self.GameBoard[0][col] == 'o':
             return -1
      if self.GameBoard[0][0] == self.GameBoard[1][1] and self.GameBoard[2][2] == self.GameBoard[1][1]:
        if self.GameBoard[1][1] == 'x':
            return 1
        elif self.GameBoard[1][1] == 'o':
            return -1
      if self.GameBoard[0][2] == self.GameBoard[1][1] and self.GameBoard[2][0] == self.GameBoard[1][1]:
        if self.GameBoard[1][1] == 'x':
          return 1
        elif self.GameBoard[1][1] == 'o':
          return -1
      for i in range(3):
        for j in range(3):
          if self.GameBoard[i][j] == '-':
              return 2
      return 0

def max(self):
      x = None
      y = None
      max_eval = -2
      Eval = self.evaluate()
      if Eval != 2:
       return (Eval, 0, 0)
      for row in range(0, 3):
       for col in range(0, 3):
         if self.GameBoard[row][col] == '-':
           self.GameBoard[row][col] = 'x'
           min_eval = self.min()[0]
           if max_eval < min_eval:
              max_eval = min_eval
              x = col
              y = row
           self.GameBoard[row][col] = '-'
      return(max_eval, x, y)

def min(self):
      x = None
      y = None
      min_eval = 2
      Eval = self.evaluate()
      if Eval != 2:
         return (Eval, 0, 0)
      for row in range(0, 3):
        for col in range(0, 3):
         if self.GameBoard[row][col] == '-':
           self.GameBoard[row][col] = 'o'
           max_eval = self.max()[0]
           if min_eval > max_eval:
             min_eval = max_eval
             x = col
             y = row
         self.GameBoard[row][col] = '-'
      return(min_eval, x, y)
