from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ExpensesVariablePage(QWidget):

    def __init__(self, finance_service):
        super().__init__()

        self.finance = finance_service

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Despesas Variáveis Page"))

        self.setLayout(layout)
        