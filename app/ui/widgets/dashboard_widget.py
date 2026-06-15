from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout()

        self.label_income = QLabel()
        self.label_expenses = QLabel()
        self.label_balance = QLabel()

        layout.addWidget(self.label_income)
        layout.addWidget(self.label_expenses)
        layout.addWidget(self.label_balance)

        self.setLayout(layout)

    def update_values(
        self,
        total_income,
        total_expenses,
        balance
    ):
        self.label_income.setText(
            f"💰 Renda Total: R$ {total_income:.2f}"
        )

        self.label_expenses.setText(
            f"💸 Despesas Totais: R$ {total_expenses:.2f}"
        )

        self.label_balance.setText(
            f"💵 Saldo Atual: R$ {balance:.2f}"
        )
