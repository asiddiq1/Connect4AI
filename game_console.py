

import connect4_console_AI 
import connectfour

#Console    

def play_game(new_game:'ConnectFourGameState'):
    '''Plays the game (console)
    '''
    print('Welcome to connect four!\n')
    connect4_console_AI.print_board(new_game)
    
    while connectfour.winning_player(new_game) == connectfour.NONE:
        connect4_console_AI.return_turn(new_game)
        new_game = connect4_console_AI.drop_or_pop(new_game, connect4_console_AI.input_words())
        connect4_console_AI.print_board(new_game)       
            
    connect4_console_AI.print_winning_player(new_game) 



if __name__ == '__main__':
    play_game(connectfour.new_game_state())

