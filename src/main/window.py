from PySide6.QtGui import (QAction, )
from PySide6.QtWidgets import (QMainWindow, QWidget, QApplication)

from src.main.parts.dialog import Dialog
from src.main.parts.inputlayout import InputLayout
from src.main.parts.toolbar import Toolbar


class Window(QMainWindow):
    barMenus, fileMenu, aboutMenu = (None, None, None)

    dialog: Dialog
    toolbar: Toolbar
    mainWidget: QWidget
    quitAction: QAction
    aboutAction: QAction
    inputLayout: InputLayout

    def __init__(self):
        """
        method constructor for main window
        """
        super(Window, self).__init__()

        self.setWindowTitle("Calculator")

        self.mainWidget = QWidget()
        self.dialog = Dialog()
        self.barMenus = self.menuBar()
        self.fileMenu = self.barMenus.addMenu('&File')
        self.aboutMenu = self.barMenus.addMenu('&About')
        self.quitAction = QAction('&Exit', self)
        self.quitAction.setShortcut('Ctrl+Q')
        self.quitAction.triggered.connect(self.eventClickQuit)
        self.aboutAction = QAction("&Version", self)
        self.aboutAction.triggered.connect(self.eventClickAbout)
        self.toolbar = Toolbar(self)
        self.inputLayout = InputLayout(self)

    def build(self):
        """
        build method to set properties and attach the widget into self class
        """
        self.dialog.build()
        self.toolbar.build()
        self.inputLayout.build()

        self.fileMenu.addAction(self.quitAction)
        self.aboutMenu.addAction(self.aboutAction)
        self.barMenus.addMenu(self.fileMenu)
        self.barMenus.addMenu(self.aboutMenu)
        self.addToolBar(self.toolbar)
        self.mainWidget.setLayout(self.inputLayout)
        self.setCentralWidget(self.mainWidget)

        self.resize(600, 400)
        self.setFixedSize(self.size())

    def eventClickQuit(self):
        """
        event click quit window
        """
        self.close()

    def eventClickClear(self):
        """
        event click clear input
        """
        self.inputLayout.onClear()

    def eventClickPaste(self):
        """
        event click paste clipboard
        """
        self.inputLayout.numberField.setText(QApplication.clipboard().text())

    def eventClickAbout(self):
        """
        event click about dialog
        """
        self.dialog.exec()
