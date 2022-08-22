from PySide6.QtWidgets import (QVBoxLayout, QLineEdit, QLabel, QComboBox)

from src.main.parts.resultlayout import ResultLayout


class InputLayout(QVBoxLayout):
    option = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']

    inputLabel: QLabel
    numberField: QLineEdit
    optionSelect: QComboBox

    resultLayout: ResultLayout

    def __init__(self):
        """
        method constructor for input layout
        """
        super(InputLayout, self).__init__()

        self.inputLabel = QLabel("Input number")
        self.inputLabel.setFixedHeight(15)
        self.numberField = QLineEdit()
        self.optionSelect = QComboBox()
        self.optionSelect.addItems(self.option)
        self.optionSelect.currentTextChanged.connect(self.eventChangedOption)

        self.resultLayout = ResultLayout(self)

    def build(self):
        """
        build method to set properties and attach the widget into self class
        """
        self.resultLayout.build()

        self.addWidget(self.inputLabel)
        self.addWidget(self.numberField)
        self.addWidget(self.optionSelect)
        self.addLayout(self.resultLayout)

        self.setSpacing(2)
        self.setContentsMargins(20, 20, 20, 20)

    def onClear(self):
        """
        event on set clear input
        """
        self.numberField.setText('')
        self.resultLayout.onClear()

    def eventChangedOption(self, value):
        """
        event when option combobox is changed
        ---
        :param value: string value
        """
        result = []
        converter = {
            'binary': 2,
            'octal': 8,
            'decimal': 10,
            'hexadecimal': 16
        }

        if value.lower() in converter and self.numberField.text() != '':
            try:
                num = int(self.numberField.text(), converter[value.lower()])
            except ValueError:
                self.resultLayout.onSetValue('invalid', 'invalid', 'invalid', 'invalid')
            else:
                self.resultLayout.onSetValue(
                    '{:0b}'.format(num),
                    '{:0o}'.format(num),
                    num,
                    '{:0x}'.format(num)
                )
