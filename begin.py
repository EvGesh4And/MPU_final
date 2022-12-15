from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
Файл begin.py является частью модуля Proc.
Описание элемента блок-схемы Начало
Отображает название элемента, которое  пользователь вводит на вкладке Основное Окна свойств блока
"""
class Begin(QWidget):
    def __init__(self, parent = None):
        """
        Метод определяет блок "Начало", его атрибуты: text - текстовое поле, node_child - для связи с нижеследующим блоком
        """
        super().__init__(parent)
        # Флаг, который задает окно поверх всех окон
        self.setGeometry(100, 100, 100, 200)
        self.text = 'Hi'
        self.label = QLabel(self.text, self)
        self.label.setGeometry(0, 0, 100, 200)
        self.setStyleSheet("border: 1px solid #05B8CC;")