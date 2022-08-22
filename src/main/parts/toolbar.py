from PySide6.QtGui import (QIcon, )
from PySide6.QtWidgets import (QToolBar, QPushButton)


class Toolbar(QToolBar):
    clear: QPushButton
    paste: QPushButton

    def __init__(self, parent: object):
        """
        method constructor for toolbar
        ---
        :param parent: parent object class
        """
        super(Toolbar, self).__init__()

        self.clear = QPushButton()
        self.clear.setIcon(QIcon('img/trash.png'))
        self.clear.setStatusTip('Clear')
        self.clear.clicked.connect(parent.eventClickClear)

        self.paste = QPushButton()
        self.paste.setIcon(QIcon('img/paste.png'))
        self.paste.setStatusTip('Paste')
        self.paste.clicked.connect(parent.eventClickPaste)

    def build(self):
        """
        build method to set properties and attach the widget into self class
        """
        self.addWidget(self.clear)
        self.addWidget(self.paste)
