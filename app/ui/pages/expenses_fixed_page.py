from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ExpensesFixedPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Despesas Fixas Page"))

        self.setLayout(layout)
        