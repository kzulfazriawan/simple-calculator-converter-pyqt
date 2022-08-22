import sys
from PySide6.QtWidgets import QApplication
from src.main.window import Window


class App:
    @staticmethod
    def main():
        mainWindow = Window()
        mainWindow.build()
        return mainWindow


if __name__ == '__main__':
    app = QApplication([])
    w = App.main()
    w.show()
    sys.exit(app.exec())
