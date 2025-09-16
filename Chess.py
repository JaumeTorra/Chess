class ChessPiece:
    def __init__(self, color, piece_type, symbol):
        self.color = color  # 'white' or 'black'
        self.piece_type = piece_type
        self.symbol = symbol
        self.has_moved = False
    
    def __str__(self):
        return self.symbol

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = 'white'
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.setup_board()
    
    def setup_board(self):
        """Configurar el tablero inicial"""
        # Piezas negras
        piece_order = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        piece_names = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        
        for i in range(8):
            self.board[0][i] = ChessPiece('black', piece_names[i], piece_order[i])
            self.board[1][i] = ChessPiece('black', 'pawn', '♟')
        
        # Piezas blancas
        white_pieces = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        for i in range(8):
            self.board[7][i] = ChessPiece('white', piece_names[i], white_pieces[i])
            self.board[6][i] = ChessPiece('white', 'pawn', '♙')
    
    def print_board(self):
        """Mostrar el tablero"""
        print("\n  a b c d e f g h")
        for i in range(8):
            print(f"{8-i} ", end="")
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    print(f"{piece} ", end="")
                else:
                    print("· ", end="")
            print(f" {8-i}")
        print("  a b c d e f g h\n")
    
    def pos_to_coords(self, pos):
        """Convertir notación ajedrez (e.g., 'e2') a coordenadas"""
        if len(pos) != 2:
            return None
        col = ord(pos[0].lower()) - ord('a')
        row = 8 - int(pos[1])
        if 0 <= col <= 7 and 0 <= row <= 7:
            return (row, col)
        return None
    
    def coords_to_pos(self, row, col):
        """Convertir coordenadas a notación ajedrez"""
        return chr(col + ord('a')) + str(8 - row)
    
    def is_valid_move(self, from_pos, to_pos):
        """Verificar si un movimiento es válido"""
        from_coords = self.pos_to_coords(from_pos)
        to_coords = self.pos_to_coords(to_pos)
        
        if not from_coords or not to_coords:
            return False
        
        from_row, from_col = from_coords
        to_row, to_col = to_coords
        
        piece = self.board[from_row][from_col]
        target = self.board[to_row][to_col]
        
        # Verificar que hay una pieza en la posición inicial
        if not piece:
            return False
        
        # Verificar que es el turno correcto
        if piece.color != self.current_player:
            return False
        
        # No puede capturar su propia pieza
        if target and target.color == piece.color:
            return False
        
        # Verificar movimiento específico de cada pieza
        if not self.is_piece_move_valid(piece, from_row, from_col, to_row, to_col):
            return False
        
        # Verificar que el movimiento no deja al rey en jaque
        if self.would_be_in_check_after_move(from_coords, to_coords):
            return False
        
        return True
    
    def is_piece_move_valid(self, piece, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es válido para el tipo de pieza"""
        piece_type = piece.piece_type
        row_diff = to_row - from_row
        col_diff = to_col - from_col
        
        if piece_type == 'pawn':
            return self.is_pawn_move_valid(piece, from_row, from_col, to_row, to_col)
        elif piece_type == 'rook':
            return self.is_rook_move_valid(from_row, from_col, to_row, to_col)
        elif piece_type == 'knight':
            return self.is_knight_move_valid(row_diff, col_diff)
        elif piece_type == 'bishop':
            return self.is_bishop_move_valid(from_row, from_col, to_row, to_col)
        elif piece_type == 'queen':
            return (self.is_rook_move_valid(from_row, from_col, to_row, to_col) or
                    self.is_bishop_move_valid(from_row, from_col, to_row, to_col))
        elif piece_type == 'king':
            return self.is_king_move_valid(row_diff, col_diff)
        
        return False
    
    def is_pawn_move_valid(self, piece, from_row, from_col, to_row, to_col):
        """Validar movimiento de peón"""
        direction = -1 if piece.color == 'white' else 1
        row_diff = to_row - from_row
        col_diff = abs(to_col - from_col)
        
        # Movimiento hacia adelante
        if col_diff == 0:
            if row_diff == direction and not self.board[to_row][to_col]:
                return True
            # Movimiento inicial de dos casillas
            if (not piece.has_moved and row_diff == 2 * direction and 
                not self.board[to_row][to_col] and not self.board[from_row + direction][from_col]):
                return True
        # Captura diagonal
        elif col_diff == 1 and row_diff == direction:
            return self.board[to_row][to_col] is not None
        
        return False
    
    def is_rook_move_valid(self, from_row, from_col, to_row, to_col):
        """Validar movimiento de torre"""
        if from_row != to_row and from_col != to_col:
            return False
        return self.is_path_clear(from_row, from_col, to_row, to_col)
    
    def is_knight_move_valid(self, row_diff, col_diff):
        """Validar movimiento de caballo"""
        return (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2)
    
    def is_bishop_move_valid(self, from_row, from_col, to_row, to_col):
        """Validar movimiento de alfil"""
        if abs(to_row - from_row) != abs(to_col - from_col):
            return False
        return self.is_path_clear(from_row, from_col, to_row, to_col)
    
    def is_king_move_valid(self, row_diff, col_diff):
        """Validar movimiento de rey"""
        return abs(row_diff) <= 1 and abs(col_diff) <= 1
    
    def is_path_clear(self, from_row, from_col, to_row, to_col):
        """Verificar que el camino está libre"""
        row_step = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        col_step = 0 if from_col == to_col else (1 if to_col > from_col else -1)
        
        current_row, current_col = from_row + row_step, from_col + col_step
        
        while (current_row, current_col) != (to_row, to_col):
            if self.board[current_row][current_col]:
                return False
            current_row += row_step
            current_col += col_step
        
        return True
    
    def would_be_in_check_after_move(self, from_coords, to_coords):
        """Verificar si el movimiento dejaría al rey en jaque"""
        # Hacer el movimiento temporalmente
        from_row, from_col = from_coords
        to_row, to_col = to_coords
        
        piece = self.board[from_row][from_col]
        target = self.board[to_row][to_col]
        
        # Realizar movimiento temporal
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        
        # Actualizar posición del rey si es necesario
        king_pos = self.white_king_pos if piece.color == 'white' else self.black_king_pos
        if piece.piece_type == 'king':
            king_pos = (to_row, to_col)
        
        # Verificar si está en jaque
        in_check = self.is_in_check(piece.color, king_pos)
        
        # Deshacer el movimiento
        self.board[from_row][from_col] = piece
        self.board[to_row][to_col] = target
        
        return in_check
    
    def is_in_check(self, color, king_pos=None):
        """Verificar si el rey está en jaque"""
        if not king_pos:
            king_pos = self.white_king_pos if color == 'white' else self.black_king_pos
        
        king_row, king_col = king_pos
        opponent_color = 'black' if color == 'white' else 'white'
        
        # Verificar todas las piezas del oponente
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    if self.is_piece_move_valid(piece, row, col, king_row, king_col):
                        return True
        
        return False
    
    def make_move(self, from_pos, to_pos):
        """Realizar un movimiento"""
        if not self.is_valid_move(from_pos, to_pos):
            return False
        
        from_coords = self.pos_to_coords(from_pos)
        to_coords = self.pos_to_coords(to_pos)
        from_row, from_col = from_coords
        to_row, to_col = to_coords
        
        piece = self.board[from_row][from_col]
        
        # Actualizar posición del rey
        if piece.piece_type == 'king':
            if piece.color == 'white':
                self.white_king_pos = to_coords
            else:
                self.black_king_pos = to_coords
        
        # Realizar el movimiento
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        piece.has_moved = True
        
        # Cambiar turno
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        
        return True
    
    def is_checkmate(self):
        """Verificar si hay jaque mate"""
        if not self.is_in_check(self.current_player):
            return False
        
        # Probar todos los movimientos posibles
        for from_row in range(8):
            for from_col in range(8):
                piece = self.board[from_row][from_col]
                if piece and piece.color == self.current_player:
                    for to_row in range(8):
                        for to_col in range(8):
                            from_pos = self.coords_to_pos(from_row, from_col)
                            to_pos = self.coords_to_pos(to_row, to_col)
                            if self.is_valid_move(from_pos, to_pos):
                                return False
        return True
    
    def is_stalemate(self):
        """Verificar si hay tablas por ahogado"""
        if self.is_in_check(self.current_player):
            return False
        
        # Verificar si hay movimientos válidos
        for from_row in range(8):
            for from_col in range(8):
                piece = self.board[from_row][from_col]
                if piece and piece.color == self.current_player:
                    for to_row in range(8):
                        for to_col in range(8):
                            from_pos = self.coords_to_pos(from_row, from_col)
                            to_pos = self.coords_to_pos(to_row, to_col)
                            if self.is_valid_move(from_pos, to_pos):
                                return False
        return True

def play_chess():
    """Función principal del juego"""
    board = ChessBoard()
    
    print("¡Bienvenido al Ajedrez!")
    print("Usa notación algebraica (ej: e2-e4)")
    print("Escribe 'quit' para salir\n")
    
    while True:
        board.print_board()
        
        # Verificar condiciones de fin del juego
        if board.is_checkmate():
            winner = 'Negras' if board.current_player == 'white' else 'Blancas'
            print(f"¡Jaque mate! Las {winner} ganan! 🏆")
            break
        
        if board.is_stalemate():
            print("¡Tablas por ahogado! 🤝")
            break
        
        if board.is_in_check(board.current_player):
            print("¡Jaque! ⚠️")
        
        # Turno del jugador
        player_name = 'Blancas' if board.current_player == 'white' else 'Negras'
        move = input(f"{player_name}, ingresa tu movimiento: ").strip().lower()
        
        if move == 'quit':
            print("¡Gracias por jugar!")
            break
        
        # Parsear el movimiento
        if '-' not in move or len(move.split('-')) != 2:
            print("Formato incorrecto. Usa: e2-e4")
            continue
        
        from_pos, to_pos = move.split('-')
        
        # Intentar hacer el movimiento
        if board.make_move(from_pos, to_pos):
            print(f"Movimiento realizado: {from_pos} -> {to_pos}")
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

if __name__ == "__main__":
    play_chess()