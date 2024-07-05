import os
import platform
import logic
import chess
import ai

orgin_board =  'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

board = logic.Board(fen = orgin_board)
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

square_size = 480 // 8
images = {True:'W',False:'B'}

if opp_color == None:
    winner = []
    moves = []
    for i in range(10):
        board = logic.Board(orgin_board)
        movess = []
        while not board.get_game_over():
            print(board.board)
            valid_moves = board.get_moves()
            
            print(board.get_whomes_turn())
            print()
            if opp_color != None:
                if images[board.get_whomes_turn()] == opp_color:
                    hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,2,max_q= True if opp_color == 'W' else False)
                    board.make_move(hio[0])
                else:
                    baller = str(input("INPUT VALID MOVE FROM VALID MOVE LIST"))
                    if chess.Move.from_uci(baller) in valid_moves:

                        board.make_move(chess.Move.from_uci(baller))
            
            elif who_am_i == '':
                if images[board.get_whomes_turn()] == 'B':
                    hio = ai_runner_black.make_move(board.get_fen(), board.board.fullmove_number - 1,2,False)
                    board.make_move(hio)
                    movess.append(hio)
                else:
                    hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,2,True)
                    board.make_move(hio)
                    movess.append(hio)                    
                
            clear_console()
        winner.append((board.board.outcome(), board.get_whomes_turn()))
        moves.append(movess)
    print(winner)
else:
    while not board.get_game_over():
            print(board.board)
            valid_moves = board.get_moves()
            
            print(board.get_whomes_turn())
            print()
            if opp_color != None:
                if images[board.get_whomes_turn()] == opp_color:
                    hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,2,max_q= True if opp_color == 'W' else False)
                    board.make_move(hio[0])
                else:
                    baller = str(input("INPUT VALID MOVE FROM VALID MOVE LIST"))
                    if chess.Move.from_uci(baller) in valid_moves:

                        board.make_move(chess.Move.from_uci(baller))
            
            elif who_am_i == '':
                if images[board.get_whomes_turn()] == 'B':
                    hio = ai_runner_black.make_move(board.get_fen(), board.board.fullmove_number - 1,2,False)
                    board.make_move(hio[0])
                else:
                    hio = ai_runner.make_move(board.get_fen(), board.board.fullmove_number - 1,2,True)
                    board.make_move(hio[0])
                    
                
            clear_console()


print(board.board)

print(moves)