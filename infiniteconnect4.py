import numpy as np
import string
import math
import random

class connect4:
    def __init__(self,size,players):
        self.size = size
        self.players = players
        self.matrix = np.zeros((self.size,self.size))
        self.count = 0
        self.val = dict(zip([(math.pow(4,n)-1)/3 for n in np.arange(1,self.players+1)],list(string.ascii_uppercase)))
        self.turn = 0
        self.choices = np.arange(self.size)
        self.state = True

    def draw(self):
        for _ in range(self.size):
            draw_row = '|'
            for i in self.matrix[_]:
                if i == 0:
                    draw_row+='_'
                else:
                    draw_row+=self.val[i]
                draw_row+='|'
            print(draw_row)

    def input(self):
        # player match (untag or tag):
        #col, row = int(input('chose a column from %d through %d: ' % (1,self.size)))-1, 0

        # Random match(untag or tag):
        col, row = random.choice(self.choices),0

        print('\n')
        for _ in range(self.size):
            if self.matrix[row][col] == 0:
                row += 1
            else:
                if row == 0:
                    print(f'column {col} is full !')
                    self.choices = np.delete(self.choices, np.argwhere(self.choices == col))
                    return self.input()
                break
        self.matrix[row-1][col] = list(self.val.keys())[self.turn%self.players]
        self.turn+=1

    def capture(self,x,y):
        capture = self.matrix[x:x+4,y:y+4]
        #print(capture)
        self.matrix_calc(capture)

    def matrix_calc(self,board):
        matrix_hor_sum = board.sum(axis=1)
        matrix_ver_sum = board.sum(axis=0)
        matrix_diag_sum = [np.trace(board), np.trace(np.flip(board,axis=1))]
        vals = np.append(matrix_hor_sum, matrix_ver_sum)
        vals = np.append(vals,matrix_diag_sum)
        #print(vals)
        for i in self.val:
            if i*4 in vals:
                self.state = False
                print(f"Player {self.val[i]} won")

    def play(self):
        self.draw()
        for _ in range(self.size**2):
            if self.state:
                self.input()
                self.draw()
                for y in range(self.size-3):
                    for x in range(self.size-3):
                        if self.state:
                            self.capture(x,y)
            else:
                return
        print('draw')
        return


game = connect4(int(input('size of board: ')),int(input('number of players: ')))
game.play()
