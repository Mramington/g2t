import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle("Hello world")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())# Наконец, мы входим в главный цикл приложения.



