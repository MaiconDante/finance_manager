from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QTextEdit
)

from app.ui.widgets.financial_card import FinancialCard

class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout()

        self.income_card = FinancialCard("💰 Renda")
        self.expense_card = FinancialCard("💸 Despesas")
        self.balance_card = FinancialCard("💵 Saldo")
        self.insights_box = QTextEdit()
        self.insights_box.setReadOnly(True)

        layout.addWidget(self.insights_box)
        layout.addWidget(self.income_card)
        layout.addWidget(self.expense_card)
        layout.addWidget(self.balance_card)

        self.setLayout(layout)

    def update_values(
        self,
        total_income,
        total_expenses,
        balance
    ):

        self.income_card.update_value(
            total_income
        )

        self.expense_card.update_value(
            total_expenses
        )

        self.balance_card.update_value(
            balance
        )

    def update_insights(self, insights):

        self.insights_box.setText(
            "\n".join(insights)
        )

    def _update_dashboard(self):

        self.dashboard.update_values(
            self.finance.total_income(),
            self.finance.total_expenses(),
            self.finance.balance()
        )

        self.dashboard.update_insights(
            self.finance.get_insights()
        )
        