import os
import platform
import logic
import time
import ai

board = logic.Board()
get_fen = board.get_fen()
who_am_i = str(input("What side do you want to play, 'White':'W' || 'Black':'B' "))
opp_color = None
if who_am_i != '':
    
    opp_color = 'W' if who_am_i == 'B' else 'B'
    ai_runner = ai.AI(get_fen, color = opp_color, one_v_one= True)
else:
    ai_runner = ai.AI(get_fen, color = 'W', one_v_one= False)
    ai_runner_black = ai.AI(get_fen, color = 'B', one_v_one=False)


def clear_console():
    if platform.system() == "Windows":
        os.system('cls') 


# pygame.init()
# screen = pygame.display.set_mode((480,480))
square_size = 480 // 8
images = {True:'W',False:'B'}


while not board.get_game_over():
    print(board.board)
    valid_moves = board.get_moves()
    
    print(board.get_whomes_turn())
    print()
    if opp_color != None:
        if images[board.get_whomes_turn()] == opp_color:
            hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,1)
            board.make_move(hio[0])
        else:
            for i in range(len(valid_moves)-1):
                print(i, valid_moves[i])
            board.make_move(valid_moves[int(input("INPUT INDEX FROM VALID MOVE LIST"))])
    
    elif who_am_i == '':
        if images[board.get_whomes_turn()] == 'B':
            hio = ai_runner_black.make_move(board.get_fen(), board.board.fullmove_number - 1,1)
            board.make_move(hio[0])
        else:
            hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,1)
            board.make_move(hio[0])
            
        
    clear_console()

print(board.board)

print(board.board.is_checkmate(), board.board.can_claim_threefold_repetition(),board.board.can_claim_fifty_moves
      ())