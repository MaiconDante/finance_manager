from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class FinanceSettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Finance Settings Page"))

        self.setLayout(layout)
