

import newconnect4 
import connectfour

#Console    

def play_game(new_game:'ConnectFourGameState'):
    '''Plays the game (console)
    '''
    print('Welcome to connect four!\n')
    newconnect4.print_board(new_game)
    
    while connectfour.winning_player(new_game) == connectfour.NONE:
        newconnect4.return_turn(new_game)
        new_game = newconnect4.drop_or_pop(new_game, newconnect4.input_words())
        newconnect4.print_board(new_game)       
            
    newconnect4.print_winning_player(new_game) 



if __name__ == '__main__':
    play_game(connectfour.new_game_state())

