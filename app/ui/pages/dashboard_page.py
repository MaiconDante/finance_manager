from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from app.ui.widgets.dashboard_widget import DashboardWidget
from app.ui.widgets.charts_widget import ChartsWidget

class DashboardPage(QWidget):

    def __init__(self, finance_service):
        super().__init__()

        self.finance = finance_service

        self._setup_ui()
        self._update_content()

    def _setup_ui(self):

        self.layout = QVBoxLayout()

        # 🔹 Cards + Insights
        self.dashboard = DashboardWidget()

        # 🔹 Gráficos
        self.charts = ChartsWidget()

        self.layout.addWidget(self.dashboard)
        self.layout.addWidget(self.charts)

        self.setLayout(self.layout)

    def _update_content(self):

        transactions = self.finance.transactions

        # Dashboard (cards + insights)
        self.dashboard.update_values(
            self.finance.total_income(),
            self.finance.total_expenses(),
            self.finance.balance()
        )

        self.dashboard.update_insights(
            self.finance.get_insights()
        )

        # Charts
        self.charts.plot_expenses_by_category(transactions)

        self.charts.plot_income_vs_expenses(
            self.finance.total_income(),
            self.finance.total_expenses()
        )
