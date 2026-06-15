from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ExpensesVariablePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Despesas Variáveis Page"))

        self.setLayout(layout)
        