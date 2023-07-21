import pygame
import MinMax_algorithm
import GUI

if __name__ == "__main__":
 
  Board = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

  G = GameDesign()
  while True:
        G.GUI(Board)
        M = MinMax(Board)
        bestmove = M.max()
        G.MakeMove(bestmove[1], bestmove[2], 'x')
        G.Result()