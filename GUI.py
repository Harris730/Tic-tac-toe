import pygame
import MinMax_algorithm
class GameDesign:
 def _init_(self):
      self.GameState = 2
      background_color = (238,106,80)
      self.foreground_color = (255, 255, 255)
      (width, height) = (600, 600)
      self.screen = pygame.display.set_mode((width, height))
      pygame.display.set_caption('TIC TAC TOE')
      self.screen.fill(background_color)
      pygame.display.flip()
 def DrawBoard(self):
     '''Draws the lines of the GameBoard'''
     for xy in range(200, 401, 200):
    # c1=(139,35,35)
        pygame.draw.line(self.screen,(139,35,35), (0, xy), (600, xy), 10)
        pygame.draw.line(self.screen,(139,35,35), (xy, 0), (xy, 600), 10)

def DrawX(self, x, y):
      x += 1
      y += 1
      pygame.draw.line(self.screen,(255,215,0), (200 * x - 200 + 10, 200 * y - 200 + 10), ((x * 200) - 10, (y 
      * 200) - 10), 7)
      pygame.draw.line(self.screen,(255,215,0), (200 * x - 200 + 10, (y * 200) - 10), ((x * 200) - 10, 200 * y 
      - 200 + 10), 7)

def DrawO(self, x, y):
      x += 1
      y += 1
      pygame.draw.circle(self.screen,(255,140,0), (x * 200 - 100, y * 200 - 100), 90, 7)
 
def MakeMove(self, x, y, player):
    if self.gameboard[y][x] == '-':
      self.gameboard[y][x] = player
      return True
    return False

def Result(self):
    self.GameState = MinMax(self.gameboard).evaluate()
    if self.GameState == 1:
      print('X Won the Game')
    elif self.GameState == 0:
      print('DRAW')
    elif self.GameState == -1:
      print('O Won the Game')

def GUI(self, gameboard):
    self.gameboard = gameboard
    while True:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          Mouse_x, Mouse_y = pygame.mouse.get_pos()
          x = round(Mouse_x/200 - 0.49)
          y = round(Mouse_y/200 - 0.49)
          self.Result()
          if self.GameState == 2:
             ValidMove = self.MakeMove(x, y,'o')
             if ValidMove:
               return self.gameboard
        if event.type == pygame.QUIT:
              pygame.quit()
        self.DrawBoard()
        for row in range(3):
          for col in range(3):
            if self.gameboard[row][col] == 'x':
              self.DrawX(col, row)
            if self.gameboard[row][col] == 'o':
              self.DrawO(col, row)
      pygame.display.update()
