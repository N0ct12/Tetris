from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QWidget, QPushButton, QSlider, QLabel, QCheckBox
from Tetris import Tetris


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tetris Menu')
        self.setGeometry(100, 100, 300, 200)
        self.center()
        self.theme = 'day'
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.setWindowIcon(QIcon('tetris.png'))
        layout = QVBoxLayout()

        # Создание ползунка для выбора скорости
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(3)
        self.speed_slider.setValue(2)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setTickPosition(QSlider.TicksBelow)
        self.speed_slider.valueChanged.connect(self.update_speed_label)
        layout.addWidget(self.speed_slider)

        # Метка для отображения выбранной скорости
        self.speed_label = QLabel('Medium')
        layout.addWidget(self.speed_label)

        # Создание переключателя для выбора темы
        self.theme_checkbox = QCheckBox('Night Mode')
        self.theme_checkbox.stateChanged.connect(self.toggle_theme)
        layout.addWidget(self.theme_checkbox)

        # Кнопка для запуска игры
        self.start_button = QPushButton('Start Game')
        self.start_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_button)

        centralWidget.setLayout(layout)

        self.tetris_game = None

    def update_speed_label(self):
        # Обновление метки скорости при изменении ползунка
        speed_value = self.speed_slider.value()
        if speed_value == 1:
            self.speed_label.setText('Slow')
        elif speed_value == 2:
            self.speed_label.setText('Medium')
        else:
            self.speed_label.setText('Fast')

    def toggle_theme(self):
        # Изменение темы при переключении переключателя
        if self.theme_checkbox.isChecked():
            self.setStyleSheet('background-color: #333; color: white;')
            self.theme = 'night'
        else:
            self.setStyleSheet('background-color: white; color: black;')
            self.theme = 'day'

    def start_game(self):
        # Запуск игры с выбранной скоростью
        speed_value = self.speed_slider.value()
        speed_mapping = {1: 800, 2: 500, 3: 300}
        self.tetris_game = Tetris(speed_mapping[speed_value],self.theme)
        self.tetris_game.show()
        self.close()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)
