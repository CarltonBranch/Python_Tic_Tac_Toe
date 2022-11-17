import random
import math


class Player:
    def __init__(self, name=""):
        self.name = name
        self.score = 0
        self.moves = []

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_moves(self):
        return self.moves

    def add_move(self, move):
        self.moves.append(move)

    def is_move_present(self, move):
        return move in self.moves


class Tile:
    def __init__(self, position):
        self.position = position
        self.played_by = ""

    def __str__(self):
        return self.position if self.played_by == "" else self.played_by


class Game:
    game_board = None
    winner = None

    def __init__(self):
        self. game_board = [[Tile('A1'), Tile('A2'), Tile('A3')], [
            Tile('B1'), Tile('B2'), Tile('B3')], [Tile('C1'), Tile('C2'), Tile('C3')]]
        self.user = Player()
        self.computer = Player()
        self.computer.moves = ['A1', 'A2', 'A3',
                               'B1', 'B2', 'B3',
                               'C1', 'C2', 'C3']

    def print_gameboard(self):
        print('========================')
        print('')
        for i in range(2):
            print("{} | {} | {}".format(
                self.game_board[i][0], self.game_board[i][1], self.game_board[i][2]))
            print("------------")
        print("{} | {} | {}".format(
            self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]))
        print('')
        print('========================\n\n')

    def select_players(self):
        player_choice = input('Do you want to be player O or player X: ')
        # handle bad input
        while player_choice.lower() != "o" and player_choice.lower() != "x":
            player_choice = input("Please enter 'X' or 'O': ")

        if player_choice.lower() == 'o':
            self.user.name = 'O'
            self.computer.name = 'X'
        else:
            self.user.name = 'X'
            self.computer.name = 'O'
        print()
        print('========================')
        print('Welcome Player {}!!'.format(self.user))
        print('You will be competing against the computer: Player {}'.format(
            self.computer))
        print('========================\n\n')

    def print_instructions():
        print("P = prints the current state of the game board")

    def is_user_input_valid(self, input):
        input = input.upper()
        if input[0] == 'A' or input[0] == 'B' or input[0] == 'C':
            if input[1] == '1' or input[1] == '2' or input[1] == '3':
                return True
        return False

    def convert_choice_to_position(self, user_choice):
        row = 0
        col = 0
        if user_choice[0] == 'A':
            row = 0
        if user_choice[0] == 'B':
            row = 1
        if user_choice[0] == 'C':
            row = 2
        if user_choice[1] == '1':
            col = 0
        if user_choice[1] == '2':
            col = 1
        if user_choice[1] == '3':
            col = 2
        return [row, col]

    def play_user_move(self, user_choice):

        matrix_index = self.convert_choice_to_position(user_choice)
        self.game_board[matrix_index[0]
                        ][matrix_index[1]].played_by = self.user.get_name()
        self.computer.get_moves().remove(user_choice)
        self.user.get_moves().append(user_choice)
        if self.check_for_winner(self.user) == False:
            self.play_computer_move()
            if self.check_for_winner(self.computer) == True:
                self.winner_found(self.computer)
        else:
            self.winner_found(self.user)
        print('game board has been updated')

    def play_computer_move(self):
        list = self.computer.get_moves()
        name = self.computer.get_name()
        length = len(list)
        choice = list[math.floor(random.randint(0, length-1))]
        matrix_index = self.convert_choice_to_position(choice)
        self.game_board[matrix_index[0]
                        ][matrix_index[1]].played_by = name

    def winner_found(self):
        return False

    def check_for_winner(self, player):
        return False

    def game_loop(self):
        while self.winner_found() == False:
            self.print_gameboard()
            user_choice = input(
                'Enter your move [Player '+self.user.get_name() + ']: ').upper()
            while self.is_user_input_valid(user_choice) == False:
                user_choice = input(
                    'Invalid input. Please enter your move: ').upper()
                self.print_gameboard()
            self.play_user_move(user_choice)

    def start_game(self):
        print('WELCOME TO TIC TAC TOE!!')
        self.print_gameboard()
        self.select_players()
        self.game_loop()


game = Game()
game.start_game()
