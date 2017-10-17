

import connectfour

#Shared 

def print_numbers():
    '''Prints the numbers 1-7
    '''
    for x in range(1, connectfour.BOARD_COLUMNS +1):
        print(x, '', end='')
    print() 



def print_board(new_game: 'ConnectFourGameState'):
    '''Prints the board of the game
    '''
    print_numbers() 
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if new_game.board[column][row] == connectfour.NONE:
                print('. ', end ='') 
            elif new_game.board[column][row] == connectfour.RED:
                print('R ',end='')
            elif new_game.board[column][row] == connectfour.YELLOW:
                print('Y ', end='')
        print()


def return_color(new_board: 'ConnectFourGameState'):
    '''Specifies the the color on the game board 
    '''
    if new_board.turn == connectfour.RED:
        return 'R'
    elif new_board.turn == connectfour.YELLOW:
        return 'Y'
    

def return_turn(new_game: 'ConnectFourGameState'):
    '''Prints out whos turn it is
    '''
    print("IT'S {}'S TURN".format(return_color(new_game)))



def input_num():
    '''Return the input of DROP/POP
    '''
    return input('INSERT DROP/POP, COLUMN NUMBER:')



def split_input(response)->list:
    '''Splits the input response and turns it into a list
    '''
    response_split = response.split()
    return response_split

       

def print_winning_player(new_game: 'ConnectFourGameState'):
    '''Returns the winning player of the game
    '''
    if connectfour.winning_player(new_game) == connectfour.RED:
        print("RED is the winner")
        
    else:
        print("YELLOW is the winner")


def input_words()->list:
    '''Returns the input splitted into a list
    '''
    input_words = split_input(input_num())
    return input_words



def drop(input_words)->bool:
    '''Returns true or false if the words in the parameter are true or false
    '''
    return input_words[0].upper() == 'DROP'


def pop(input_words)->bool:

    return input_words[0].upper() == 'POP'
        
    

def drop_or_pop(new_game:'ConnectFourGameState', input_words:list)->'ConnectFourGameState':
    '''Returns a new game state if the pieces are either dropped or popped
    '''
    try: 
        if drop(input_words): 
            new_game = connectfour.drop_piece(new_game, int(input_words[1])-1)
            return new_game
        
        elif pop(input_words):
            new_game = connectfour.pop_piece(new_game, int(input_words[1])-1)
            return new_game
        else:
            print('Invalid move. Try again.')
            print()
            return new_game


    except:
        print('Not a valid input. Try again.')
        print() 
        return new_game 
      

    

