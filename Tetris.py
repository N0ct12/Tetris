from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from Board import Board


class Tetris(QMainWindow):

    def __init__(self, speed, theme):
        super().__init__()

        self.initUI(speed,theme)

    def initUI(self, speed, theme):
        self.tboard = Board(self, speed, theme)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msgToStatus[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(400, 700)
        self.center()
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('tetris.png'))
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

