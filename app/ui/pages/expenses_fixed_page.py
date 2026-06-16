from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ExpensesFixedPage(QWidget):

    def __init__(self, finance_service):
        super().__init__()

        self.finance = finance_service

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Despesas Fixas Page"))

        self.setLayout(layout)
        