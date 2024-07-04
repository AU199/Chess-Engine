import chess, chess.svg




class Board:
    def __init__(self):
        self.board =chess.Board()
    def check_promotion(self):
 
        for move in self.board.legal_moves:
            if chess.Move.promotion(move):
                return True
        return False
        
    def get_moves(self):
        return list(self.board.legal_moves)
    def get_game_over(self):
        return self.board.is_game_over()
    def make_move(self, move):
        self.board.push(move)
    def get_whomes_turn(self):
        return self.board.turn

    def get_fen(self):
        return self.board.fen()
    
    def change_to_uci(self,string_to:str):
        return chess.Move.uci(string_to)
    def is_it_checkMate(self):
        return self.board.is_checkmate()