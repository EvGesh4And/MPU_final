from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
Файл Development.py является частью модуля Proc.
Основное окно, в котором пользователь может собрать блок-схему.
Содержит меню, в котором представлены функции программы
"""


class Development(QMainWindow):
    def __init__(self, parent):
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

        # Вызов команд при нажатии на кнопки
        # self.create.triggered.connect(self.CreateFile)

        # Создание вложенных списков
        self.add_elem = self.menubar.addMenu("Добавить элемент")
        self.begin1 = self.add_elem.addAction("Начало")
        self.operation = self.add_elem.addAction("Операция")
        self.condition1 = self.add_elem.addAction("Условие")
        self.end = self.add_elem.addAction("Конец")

        # Вызов команд при нажатии на кнопки
        # self.begin1.triggered.connect(self.add_begin)

        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(grey.png)}")
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("grey.png")))
        self.setPalette(self.palette)
        # self.help = Help()

        self.indicator_begin = ""
        self.indicator_end = ""
        self.indicator_pairs = {}
        self.indicator_begins = []
        self.indicator_ends = []

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.slot_timer_timeout)

    def slot_timer_timeout(self):
        self.update()
