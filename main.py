from random import randint
import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication
)
from PyQt5.QtGui import (
    QPainter,
    QColor
)
from window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._should_draw = False
        self.setupUI(self)
        self._init_ui()

    def _init_ui(self) -> None:
        self.create_button.clicked.connect(self._create)

    def _create(self):
        self._should_draw = True
        self.update()

    def paintEvent(self, event) -> None:
        if not self._should_draw:
            return

        qr = QPainter()
        qr.begin(self)
        self.draw_circle(qr)
        qr.end()

    def draw_circle(self, qr):
        qr.setBrush(QColor('yellow'))
        diameter = randint(70, 200)
        start = 60
        qr.drawEllipse(start, start, start + diameter, start + diameter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
exit_code = app.exec()
sys.exit(exit_code)
