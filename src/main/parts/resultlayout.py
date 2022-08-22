from PySide6.QtWidgets import (QFormLayout, QLineEdit)


class ResultLayout(QFormLayout):
    binary: QLineEdit
    octal: QLineEdit
    decimal: QLineEdit
    hexadecimal: QLineEdit

    def __init__(self):
        """
        method constructor for result layout
        """
        super(ResultLayout, self).__init__()

        self.binary = QLineEdit()
        self.binary.setReadOnly(True)
        self.octal = QLineEdit()
        self.octal.setReadOnly(True)
        self.decimal = QLineEdit()
        self.decimal.setReadOnly(True)
        self.hexadecimal = QLineEdit()
        self.hexadecimal.setReadOnly(True)

    def build(self):
        """
        build method to set properties and attach the widget into self class
        """
        self.addRow('Binary:', self.binary)
        self.addRow('Octal:', self.octal)
        self.addRow('Decimal:', self.decimal)
        self.addRow('Hexadecimal:', self.hexadecimal)

        self.setContentsMargins(0, 50, 0, 0)
        self.setSpacing(7)

    def onSetValue(self, *args):
        """
        event on set value field
        ---
        :param args: argument value
        """
        self.binary.setText(str(args[0]))
        self.octal.setText(str(args[1]))
        self.decimal.setText(str(args[2]))
        self.hexadecimal.setText(str(args[3]))

    def onClear(self):
        """
        event on clearing field value
        """
        self.onSetValue('', '', '', '')
