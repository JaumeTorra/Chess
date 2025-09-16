# ♔ Chess Game in Python

A fully functional chess game implemented in Python with complete rule validation, check/checkmate detection, and an intuitive console interface. Experience the classic strategy game right in your terminal!

## ✨ Features

### 🎯 Complete Chess Implementation
- **All Standard Pieces** - King, Queen, Rook, Bishop, Knight, and Pawn with authentic movement patterns
- **Rule Validation** - Full implementation of official chess rules and move validation
- **Check Detection** - Automatic detection and prevention of moves that leave the king in check
- **Game End Conditions** - Checkmate and stalemate detection with automatic game termination
- **Turn Management** - Proper alternating turns between white and black players

### 🎨 User Experience
- **Unicode Chess Pieces** - Beautiful visual representation using ♔♕♖♗♘♙ symbols
- **Algebraic Notation** - Standard chess notation (e.g., e2-e4) for move input
- **Clear Board Display** - Clean 8x8 grid with coordinate labels (a-h, 1-8)
- **Game Status Updates** - Real-time notifications for check, checkmate, and stalemate
- **Input Validation** - Robust error handling and user guidance

### 🧠 Advanced Logic
- **Path Validation** - Intelligent pathfinding for sliding pieces (rook, bishop, queen)
- **Piece-Specific Movement** - Each piece type follows its unique movement rules
- **King Safety** - Prevents any move that would result in check
- **Game State Tracking** - Maintains complete game state including piece positions and move history

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required!

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/python-chess-game.git
cd python-chess-game

# Run the game
python chess_game.py
```

## 🎮 How to Play

### Starting the Game
```bash
python chess_game.py
```

### Game Controls
- **Move Format**: Use algebraic notation (e.g., `e2-e4`)
- **Quit Game**: Type `quit` at any time
- **Coordinate System**: 
  - Files (columns): a-h (left to right)
  - Ranks (rows): 1-8 (bottom to top)

### Board Layout
```
  a b c d e f g h
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7
6 · · · · · · · · 6
5 · · · · · · · · 5
4 · · · · · · · · 4
3 · · · · · · · · 3
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1
  a b c d e f g h
```

### Example Gameplay
```
Blancas, ingresa tu movimiento: e2-e4
Movimiento realizado: e2 -> e4

  a b c d e f g h
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7
6 · · · · · · · · 6
5 · · · · · · · · 5
4 · · · · ♙ · · · 4
3 · · · · · · · · 3
2 ♙ ♙ ♙ ♙ · ♙ ♙ ♙ 2
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1
  a b c d e f g h

Negras, ingresa tu movimiento: d7-d5
```

## 🏗️ Code Architecture

### Core Classes

#### `ChessPiece`
Represents individual chess pieces with properties:
```python
class ChessPiece:
    def __init__(self, color, piece_type, symbol):
        self.color = color          # 'white' or 'black'
        self.piece_type = piece_type # 'pawn', 'rook', etc.
        self.symbol = symbol         # Unicode chess symbol
        self.has_moved = False       # For special moves tracking
```

#### `ChessBoard`
Main game engine handling:
- Board state management
- Move validation and execution
- Check/checkmate detection
- Game flow control

### Key Methods

| Method | Purpose |
|--------|---------|
| `setup_board()` | Initialize starting chess position |
| `is_valid_move()` | Comprehensive move validation |
| `is_piece_move_valid()` | Piece-specific movement rules |
| `is_in_check()` | Check detection algorithm |
| `is_checkmate()` | Checkmate detection algorithm |
| `make_move()` | Execute validated moves |

### Movement Validation

Each piece type has specialized validation:

- **Pawn** - Forward movement, diagonal capture, initial two-square move
- **Rook** - Horizontal and vertical lines with path clearing
- **Bishop** - Diagonal lines with path clearing  
- **Knight** - L-shaped moves (2+1 or 1+2 squares)
- **Queen** - Combined rook and bishop movement
- **King** - One square in any direction

## 🧪 Game Logic Examples

### Check Detection
```python
def is_in_check(self, color, king_pos=None):
    """Verify if the king is in check"""
    # Scan all opponent pieces
    # Test if any can capture the king
    # Return True if king is threatened
```

### Move Validation Pipeline
1. **Basic Validation** - Valid coordinates, piece ownership
2. **Piece Rules** - Movement pattern validation
3. **Path Clearing** - No pieces blocking the path
4. **Check Prevention** - Move doesn't expose own king
5. **Execute** - Update board state and switch turns

## 🎯 Game Features Status

| Feature | Status | Description |
|---------|--------|-------------|
| ✅ Basic Movement | Complete | All pieces move according to chess rules |
| ✅ Check Detection | Complete | Prevents illegal moves, detects check |
| ✅ Checkmate | Complete | Automatic game end detection |
| ✅ Stalemate | Complete | Draw condition detection |
| ⏳ Castling | Planned | King and rook special move |
| ⏳ En Passant | Planned | Pawn capture special rule |
| ⏳ Pawn Promotion | Planned | Pawn to queen/rook/bishop/knight |
| ⏳ AI Opponent | Planned | Single player vs computer |

## 🚀 Future Enhancements

### Phase 1 - Complete Rule Set
- [ ] **Castling** - King and rook coordinated move
- [ ] **En Passant** - Special pawn capture
- [ ] **Pawn Promotion** - Transform pawns reaching the end
- [ ] **Draw Conditions** - 50-move rule, repetition, insufficient material

### Phase 2 - Enhanced Gameplay  
- [ ] **Move History** - Complete game notation recording
- [ ] **Undo/Redo** - Take back moves
- [ ] **Save/Load Games** - Game persistence
- [ ] **Time Controls** - Chess clocks and time limits

### Phase 3 - AI & Advanced Features
- [ ] **AI Engine** - Computer opponent with difficulty levels
- [ ] **Opening Database** - Common opening moves
- [ ] **Position Analysis** - Evaluate board positions
- [ ] **Puzzle Mode** - Chess tactics trainer

### Phase 4 - User Interface
- [ ] **GUI Version** - Pygame or Tkinter interface
- [ ] **Web Interface** - Browser-based chess
- [ ] **Mobile App** - Smartphone compatibility
- [ ] **Online Multiplayer** - Network play capability

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Development Setup
```bash
git clone https://github.com/yourusername/python-chess-game.git
cd python-chess-game
python -m pytest tests/  # Run tests (when added)
```

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add comprehensive docstrings to new functions
- Include unit tests for new features
- Update documentation for significant changes
- Create detailed pull request descriptions

### Priority Contributions
1. **Special Moves Implementation** (castling, en passant, promotion)
2. **Test Suite Development** - Unit tests for game logic
3. **Performance Optimization** - Algorithm improvements
4. **Documentation** - Code comments and user guides
5. **Bug Reports** - Issue identification and reproduction

## 🔧 Technical Details

### Performance Characteristics
- **Move Generation**: O(n²) for piece scanning
- **Check Detection**: O(n²) worst case
- **Checkmate Detection**: O(n⁴) exhaustive search
- **Memory Usage**: Minimal - single board state

### Code Quality
- **Object-Oriented Design** - Clean separation of concerns
- **Type Safety** - Consistent data types and validation
- **Error Handling** - Robust input validation and error recovery
- **Modularity** - Easy to extend and modify

## 📊 Project Statistics

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-~400-yellow.svg)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License - Feel free to use, modify, and distribute
```

## 👨‍💻 Author

**[Jaume Torra]**
- 🌐 GitHub: [@JaumeTorra](https://github.com/JaumeTorra)
- 📧 Email: jaumetorra.pro@gmail.com


## 🙏 Acknowledgments

- **Chess Programming Community** - For algorithms and best practices
- **Unicode Consortium** - For chess piece symbols (♔♕♖♗♘♙)
- **Python Community** - For excellent documentation and libraries
- **FIDE** - For official chess rules and regulations

## 📚 Resources

### Chess Programming
- [Chess Programming Wiki](https://www.chessprogramming.org/)
- [Lichess Analysis](https://lichess.org/analysis) - For testing positions
- [Chess.com](https://www.chess.com/) - Rules reference

### Python Development
- [Python Chess Library](https://python-chess.readthedocs.io/) - Advanced chess programming
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Testing](https://docs.python.org/3/library/unittest.html)

---

## 🎲 Quick Start Commands

```bash
# Clone and run
git clone https://github.com/yourusername/python-chess-game.git
cd python-chess-game && python chess_game.py

# Example moves to try
# White: e2-e4, d2-d4, g1-f3
# Black: e7-e5, d7-d5, b8-c6
```

**⭐ Star this repository if you enjoy chess and clean Python code!**

*"Chess is the struggle against error." - Johannes Zukertort* ♟️
