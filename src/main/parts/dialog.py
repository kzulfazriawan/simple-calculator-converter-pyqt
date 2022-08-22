from PySide6.QtWidgets import (QDialog, QLabel, QVBoxLayout)
from PySide6.QtCore import Qt


class Dialog(QDialog):
    layout: QVBoxLayout
    label: list

    def __init__(self):
        """
        method constructor for dialog
        """
        super(Dialog, self).__init__()

        self.layout = QVBoxLayout()
        self.label = [
            QLabel("Author: Kzulfazriawan"),
            QLabel("Github: https://github.com/kzulfazriawan")
        ]

    def build(self):
        """
        build method to set properties and attach the widget into self class
        """
        for item in self.label:
            self.layout.addWidget(item)
        self.setLayout(self.layout)
        self.setWindowTitle("About")
        self.setWindowModality(Qt.ApplicationModal)
