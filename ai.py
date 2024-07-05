from types import NoneType
import random
import chess



class AI:
    def __init__(self, fen, color, one_v_one: bool):
        self.board = chess.Board(fen=fen)
        self.color = color
       
        self.piece_value = {chess.PAWN: 1, chess.BISHOP: 3, chess.KNIGHT: 3, chess.KING: 200, chess.QUEEN: 9, chess.ROOK: 5}
        self.a_moves = 0
        self.turn = {True:'W',False:'B'}
        self.one_v_one = one_v_one
        self.index = -1
        
    def eval(self, board) -> float:
            
            if board.is_checkmate(): return 1000.0
            all_scores = []
            
            score_through_it = []
            score = 0
            for square in chess.SQUARES:
                    piece = board.piece_at(square)
                    if piece:
                        
                        if piece.color == chess.WHITE:
                            score += self.piece_value[piece.piece_type] 
                        else:
                           
                            score -= self.piece_value[piece.piece_type] 

            return score
    
    
    def minMax(self,fen,depth, alpha, beta,Maximising:bool):
        
        """
        This function is called by the make move function in order to evaluate a tree of all possible moves after devling into it by the given depth
        
        Args:
            fen(String): The FEN of the current Position 
            depth(Integer): The depth that the function needs to recurse too
            alpha(Integer): The current highest value found in the tree, if the current value is greater, than we break out of the loop and return the 
            beta(Integer): The current lowest value found in the tree, if the current value is less than alpha, we break out of the loop
            Maximising(Bool): Are we maximising for ourselves

        Returns:
            Float: Returns the best evaluation of the move
        """
        
        
        
        
        
        
        
        board = chess.Board(fen=fen)
        
        if board.is_game_over() or depth == 0:
            if not board.is_checkmate():
                return self.eval(board)
            if board.is_checkmate() and Maximising:
                return 1000000
            elif board.is_checkmate() and not Maximising:
                return -1000000

        
        if Maximising:
            curr_best = -1000 
            val_moves = list(board.generate_legal_moves())
            val = 0
            
            for i in range(board.legal_moves.count()):
                move = val_moves[i]
                board.push(move= move)
                if board.can_claim_draw():
                    return -100000 if self.color == 'W' else 1000000
                val = self.minMax(board.fen(),depth= depth - 1, alpha = alpha, beta=beta,Maximising=False) if self.color == 'B' else self.minMax(board.fen(),depth= depth - 1, alpha = alpha, beta=beta,Maximising=False) 
                board.pop()
                
                if val > curr_best:
                    curr_best = val
                
                alpha = max(alpha, val)
                if beta <= alpha:
                        break   
            return curr_best
        else:
            
            curr_best = 1000
            val_moves = list(board.legal_moves)
            
            for move in val_moves:
                board.push(move= move)
                val = self.minMax(board.fen(),depth= depth - 1, alpha = alpha, beta=beta, Maximising=True)
                board.pop()
                if val is NoneType:
                    return val
                if val < curr_best:
                    curr_best = val
                beta = min(beta, val)
                
                if beta <= alpha:
                    break
            return curr_best

    def make_move(self, fen, a_moves, depth, max_q):
        
        
        
        """
        This is the main function used to find and return the best move

        Args:
            fen (String): The current FEN of the board
            a_moves (Integer): The amount of moves played in the game until now 
            depth (Int): The depth we want to search
            max_q (Bool): Whether or not we are currently maximising for ourselves.

        Returns:
            Move.uci(): Returns the best move from the list of all legal moves in a given position
        """
        
        
        
        board = chess.Board(fen)
        legal_moves = list(board.legal_moves)
        self.a_moves = a_moves
        best_val = -100 if self.color == 'W' else 100
        all_v = []
        bestIndex = 0
        white_pawn_opening_moves = ['e2e4','d2d4',  'c2c4',  'f2f4',  'g2g3']
        black_pawn_opening_moves = [['e7e5', 'c7c5', 'e7e6', 'c7c6', 'd7d6'],['d7d5', 'g8f6', 'e7e6', 'c7c6', 'd7d6'],['e7e5', 'c7c5', 'g8f6', 'c7c6', 'd7d6'], ['e7e5', 'd7d5', 'g8f6'],['d7d5', 'c7c5', 'e7e5']]

        if a_moves > 0 or self.one_v_one :
            for i in range(len(legal_moves)):
                move = legal_moves[i]
                board.push(move=move)
                val = self.minMax(board.fen(),depth=depth, alpha= -1000 , beta= 1000 ,Maximising=max_q)
                all_v.append(val)
                board.pop()
                if (val > best_val and self.color == "W") or (val < best_val and self.color == 'B') :
                    best_val = val
                    bestIndex = i
            return legal_moves[bestIndex]
        else:
            self.index = random.randint(0,len(white_pawn_opening_moves)-1)
            if board.turn:
                return chess.Move.from_uci(white_pawn_opening_moves[self.index])
            else:
                return chess.Move.from_uci(black_pawn_opening_moves[self.index][random.randint(0,len(black_pawn_opening_moves[self.index])-1)])

            
