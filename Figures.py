import os

import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint
from typing import Dict, List, Tuple
import math

from abc import ABC, abstractmethod


class BaseFigure:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # @abstractmethod         # Нужен для создания абстрактного класса, чтобы добавить дополнительную проверку:
    # вызвана ли абстрактная переменная или нет
    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError


class Rectangle(BaseFigure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y)
        self.width = w
        self.height = h

    def perimeter(self):
        return 2 * (self.width + self.height)

    def square(self):
        return self.width * self.height


class CloseFigure(BaseFigure):
    def __init__(self, coord: List[Dict[str, int]]):
        super().__init__(coord[0]["x"], coord[0]["y"])
        self._coords = coord

    def __iter__(self):
        return iter(self._coords)


class Ellipse(BaseFigure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y)
        self.width = w
        self.height = h

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.height**2 + self.width**2) / 8)

    def square(self):
        return math.pi * self.width * self.height / 4


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.setMinimumWidth(3000)
        self.setMinimumHeight(2000)
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):

        painter = QPainter(self)
        # reset_brush = painter.brush()

        for figure in self.__figures:
            if not isinstance(figure, BaseFigure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))

                points = []
                for point in figure:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue

def some_func(figures: List[BaseFigure]):
    for figure in figures:
        print(figure.square(), figure.perimeter())


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)

    figure_widget = FigureWidget()
    figures = [
        Rectangle(400, 100, 500, 300),
        Ellipse(900, 500, 600, 900),
        # Rectangle(20, 30, 400, 200),
        CloseFigure([{'x': 100, "y": 200}, {'x': 150, "y": 220}, {'x': 400, "y": 420}, {'x': 900, "y": 1600}])
    ]

    figure_widget.set_figures(figures)
    figure_widget.show()

    sys.exit(app.exec_())

