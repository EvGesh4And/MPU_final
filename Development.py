from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from begin import *

"""
Файл Development.py является частью модуля Proc.
Основное окно, в котором пользователь может собрать блок-схему.
Содержит меню, в котором представлены функции программы
"""


class Development(QMainWindow):
    def __init__(self, parent = None):
        """
        Метод определяет Главное окно
        """
        super().__init__(parent)

        # Создание вложенных списков
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)
        self.menubar.setObjectName("menubar")

        self.menu = self.menubar.addMenu("Меню")
        self.get_names = self.menu.addAction("Получить имена тэгов")
        self.save = self.menu.addAction("Сохранить файл")
        self.open = self.menu.addAction("Открыть файл")


        # Создание вложенных списков
        self.add_elem = self.menubar.addMenu("Добавить элемент")
        self.begin = self.add_elem.addAction("Начало")
        self.operation = self.add_elem.addAction("Операция")
        self.condition1 = self.add_elem.addAction("Условие")
        self.end = self.add_elem.addAction("Конец")

        # Вызов команд при нажатии на кнопки
        self.begin.triggered.connect(self.add_begin)

        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(grey.png)}")
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("grey.png")))
        self.setPalette(self.palette)

        self.indicator_begin = ""
        self.indicator_end = ""
        self.indicator_pairs = {}
        self.indicator_begins = []
        self.indicator_ends = []

    def add_begin(self):
        """
        Метод создания элемента класса Начало
        :return: виджет на главном окне
        """
        print('Hee')
        self.begin = Begin(self)
        self.begin.show()

if __name__ == "__main__":
    app = QApplication([''])
    window = Development()
    window.show()
    app.exec_()