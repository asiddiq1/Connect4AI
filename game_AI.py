import connect_socket 
import connect4_console_AI
import connectfour 

#Protocol 

def user_interface():
    '''Connects to the server, raises exception if fails, returns a socket
    '''


    host = connect_socket.read_host()
    port = connect_socket.read_port()


    try: 
        print('Connecting to {} (port {})...'.format(host, port))
        connection = connect_socket.connect(host, port)
        print('Connected')
   
    except:
        print("Sorry can't connect.")
        return None 

    else:
        input_username(connection)
        connect_socket.send_message(connection, 'AI_GAME')
        return connection



def input_username(socketcon):
    '''Input valid username to proceed to the game
    '''
    
    while True:

        message = connect_socket.username()

        if ' ' in message:
            print('Invalid username. Try again') 
        else:
            connect_socket.send_message(socketcon, 'I32CFSP_HELLO {}'.format(message))
            response = connect_socket.recieve_message(socketcon)
            return response 




def user_move(socketcon, new_game):
    '''Client makes the move
    '''
    response_ready = connect_socket.recieve_message(socketcon)
    while connect4_console_AI.return_color(new_game) == 'R':
         command_input = connect4_console_AI.input_words() 
         join_command = ' '.join(command_input).upper()
         new_game = connect4_console_AI.drop_or_pop(new_game, command_input)
    connect_socket.send_message(socketcon, join_command)
    return new_game 


def server_response(socketcon, new_game):
    '''Servers response once the client makes the move
    '''
    response = connect_socket.recieve_message(socketcon)
    
    if response == 'OKAY':
        pass
    elif response == 'INVALID':
        print('Please try again')
        return new_game

    elif response.split('_')[0] == 'WINNER':
        connect4_console_AI.print_winning_player(new_game) 
            


def AI_move(new_game, socketcon):
    '''Server makes the move
    '''

    response = connect_socket.recieve_message(socketcon)
    new_game = connect4_console_AI.drop_or_pop(new_game, response.split())
    return new_game 

    
def play_GAME(socketcon, new_game):
    '''Pulls all functions back in to play the game
    '''

        
    print('\nWELCOME TO CONNECT FOUR!') 
    connect4_console_AI.print_board(new_game) 

    while connectfour.winning_player(new_game) == connectfour.NONE:
        
        connect4_console_AI.return_turn(new_game) 
        new_game = user_move(socketcon, new_game)
        server_response(socketcon, new_game)
        new_game = AI_move(new_game, socketcon)
        connect4_console_AI.print_board(new_game) 
    connect4_console_AI.print_winning_player(new_game)
    connect_socket.close_sockets(socketcon)



    
if __name__ == '__main__':
    socketcon = user_interface()
    if socketcon != None: 
        play_GAME(socketcon, connectfour.new_game_state())
 



 
