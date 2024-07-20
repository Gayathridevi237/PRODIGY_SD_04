import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class SudokuSolverGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sudoku Solver')
        self.grid = QGridLayout()
        self.board = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.board[i][j] = QLineEdit()
                self.board[i][j].setMaxLength(1)
                self.board[i][j].setFixedSize(40, 40)
                self.board[i][j].setStyleSheet("font-size: 20px;")
                self.grid.addWidget(self.board[i][j], i, j)

        self.solve_button = QPushButton('Solve', self)
        self.solve_button.clicked.connect(self.solve)
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clear_grid)

        vbox = QVBoxLayout()
        vbox.addLayout(self.grid)
        vbox.addWidget(self.solve_button)
        vbox.addWidget(self.clear_button)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 400, 400)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                text = self.board[i][j].text()
                if text.isdigit():
                    row.append(int(text))
                else:
                    row.append(0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.board[i][j].setText(str(board[i][j]))
                else:
                    self.board[i][j].clear()

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].clear()

    def solve(self):
        board = self.get_board()
        if self.solve_sudoku(board):
            self.set_board(board)
        else:
            QMessageBox.warning(self, "Error", "No solution exists")

    def find_empty_location(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, board, num, pos):
        # Check row
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve_sudoku(self, board):
        empty_location = self.find_empty_location(board)
        if not empty_location:
            return True
        else:
            row, col = empty_location

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0

        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SudokuSolverGUI()
    ex.show()
    sys.exit(app.exec_())
