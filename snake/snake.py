'''-------------------------------'''
'''----------Sssssnake------------'''
'''-------------------------------'''

import random
import time

BOARD_SIZE = 20 #Size of the board we play snakes on

def random_vector(n=BOARD_SIZE):
    '''create a vector of two random numbers'''
    rand_y = random.randrange(n)
    rand_x = random.randrange(n)
    return (rand_y, rand_x)

class Board:

    def __init__(self, board_dimension, food, snake):
        self.n = board_dimension
        self.food = food
        self.snake = snake
        self.blank_char = '.'
        self.board = []
        self.create(self.n)        
    
    def create(self, n):
        '''Create an n x n board with a list representing X and Y: list[y][x]'''
        for y in range(n):
            x_line = []
            for x in range(n):
                x_line.append(self.blank_char)
            self.board.append(x_line)

    def update(self):
        for iy, y in enumerate(self.board):
            for ix, x in enumerate(y):
                self.board[iy][ix] = self.blank_char
##        snake_y, snake_x = self.snake.get_vect()    
##        self.board[snake_y][snake_x] = self.snake.char
##        food_y, food_x = self.food.get_vect()    
##        self.board[food_y][food_x] = self.food.char

    def __str__(self):
        self.board_string = ''
        for i, y in enumerate(self.board):
            for x in self.board[i]:
                self.board_string += x + ' '
            self.board_string += '\n'
        return self.board_string

    def erase(self):
        print('\b')

        
        

class GameCharacter:

    def __init__(self, char):
        self.vect = (0,0)
        self.y, self.x = self.vect[0], self.vect[1]
        self.char = char

    def get_vect(self):
        return self.vect
    
    def set_vect(self, given_vect):
        self.vect = given_vect
        self.y, self.x = self.vect

    def draw(self, board):
        board.board[self.y][self.x] = self.char 
    
    

class Food(GameCharacter):
    
    def __init__(self, char):
        GameCharacter.__init__(self,char)
        
        
class Snake(GameCharacter):
    
    def __init__(self, char):
        GameCharacter.__init__(self, char)
        self.bodylength = 1
        self.body_vect_list = [self.get_vect()]

    def add_new_body_segment(self):
        self.body_vect_list.append(self.get_vect())
        self.bodylength += 1

    def move(self, vect):
        self.set_vect(vect)
        if self.bodylength > 1:
            for i in range(self.bodylength):
                self.bodylength[i+1] = self.bodylength[i]

    def draw(self, board):
        for i in self.body_vect_list:
            board.board[i[0]][i[1]] = self.char
                

    def hunt_move(self, board, food):
        if food.get_vect()[0] < snake.get_vect()[0]:
            snake.move((snake.get_vect()[0]-1, snake.get_vect()[1]))
        elif food.get_vect()[0] > snake.get_vect()[0]:
            snake.move((snake.get_vect()[0]+1, snake.get_vect()[1]))
        elif food.get_vect()[1] < snake.get_vect()[1]:
            snake.move((snake.get_vect()[0], snake.get_vect()[1]-1))
        elif food.get_vect()[1] > snake.get_vect()[1]:
            snake.move((snake.get_vect()[0], snake.get_vect()[1]+1))
        

class Game:

    def __init__(self, board=Board, food=Food, snake=Snake):
        self.board = board
        self.food = food
        self.snake = snake

    def cycle(self):
        print("\033c")
        print(board)
        board.update()
        self.food.draw(self.board)
        self.snake.draw(self.board)
        snake.hunt_move(self.board, self.food)
        if self.snake.get_vect() == self.food.get_vect():
            self.food.set_vect(random_vector(BOARD_SIZE))
            self.snake.add_new_body_segment()
        time.sleep(0.2)

    def place_food(self, food, vector):
        food.set_vect(vector)
        y, x = food.get_vect()

    def place_snake(self, snake, vector):
        snake.set_vect(vector)
        y,x = snake.get_vect()
        if self.board.board[y][x] != food.char:
            self.board.board[y][x] = snake.char
        else:
            self.place_snake(self.snake)

    def initialise_level(self):
        self.place_food(self.food, random_vector())
        self.place_snake(self.snake, random_vector())

snake = Snake('$')
food = Food('F')
board = Board(BOARD_SIZE, food, snake)
game = Game(board, food, snake)
game.initialise_level()
while True:
    game.cycle()
