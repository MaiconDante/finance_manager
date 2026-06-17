from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QLabel
)

from app.ui.widgets.financial_card import FinancialCard

class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # 👈 espaço entre blocos
        main_layout.setContentsMargins(10, 20, 10, 20)

        # ===== CARDS =====
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(10) # 👈 espaço entre os cards

        self.balance_card = FinancialCard("💵 Saldo", "balance")
        self.income_card = FinancialCard("💰 Renda", "income")
        self.expense_card = FinancialCard("💸 Despesas", "expense")

        cards_layout.addWidget(self.balance_card)
        cards_layout.addWidget(self.income_card)
        cards_layout.addWidget(self.expense_card)

        # ===== INSIGHTS =====
        self.insights_title = QLabel("📊 Insights Financeiros")

        self.insights_box = QTextEdit()
        self.insights_box.setReadOnly(True)
        self.insights_box.setFixedHeight(120)  # altura mínima para mostrar vários insights

        # ===== ADD TO LAYOUT =====
        main_layout.addLayout(cards_layout)
        main_layout.addWidget(self.insights_title)
        main_layout.addWidget(self.insights_box)

        self.setLayout(main_layout)

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

        self.insights_box.clear()

        for i in insights:

            text = i["text"]
            type_ = i["type"]

            if "economizou" in text.lower():

                prefix = "💰 "

            elif type_ == "success":
                prefix = "🟢 "

            elif type_ == "warning":
                prefix = "🟡 "

            elif type_ == "danger":
                prefix = "🔴 "

            else:
                prefix = "ℹ️ "

            self.insights_box.append(prefix + text)
        