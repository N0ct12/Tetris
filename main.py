import sys

from mainMenu import Menu
from PyQt5.QtWidgets import QApplication


# todo для 50 за 5 таск:
#   1) избавиться от isPaused или isStarted -done
#   2) сделать настройки (увеличение скорости по очкам) -Done
# todo для бонуса к 6 таску (-frontend)
#   1) темная-светлая тема (вынести цвета либо в dict, либо в файл)-Done
#   2) зависимость cкорости от очков -Done
#   3) вынести все это из одного python файла -done


if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
