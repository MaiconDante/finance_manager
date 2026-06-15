from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout
)

# Importações dos widgets personalizados
from app.services.finance_service import FinanceService
from app.ui.transaction_dialog import TransactionDialog
from app.models.transaction import Transaction
from app.ui.widgets.transactions_table import TransactionsTable
from app.ui.widgets.dashboard_widget import DashboardWidget
from app.ui.widgets.charts_widget import ChartsWidget

# Janela principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance Manager")
        self.setMinimumSize(900, 600)

        # serviço central do sistema
        self.finance = FinanceService()

        # Inicializa a interface
        self._init_ui()
        self._update_dashboard()

    # Configura a interface do usuário
    def _init_ui(self):
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Título
        self.title = QLabel("📊 Dashboard Financeiro")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.title)

        # Widget dos gráficos
        self.charts = ChartsWidget()
        self.layout.addWidget(self.charts)

        # Widget do dashboard
        self.dashboard = DashboardWidget()
        self.layout.addWidget(self.dashboard)

        # Botões
        buttons_layout = QHBoxLayout()

        btn_income = QPushButton("Adicionar Renda")
        btn_expense = QPushButton("Adicionar Despesa")

        btn_income.clicked.connect(self._add_income)
        btn_expense.clicked.connect(self._add_expense)

        buttons_layout.addWidget(btn_income)
        buttons_layout.addWidget(btn_expense)

        self.layout.addLayout(buttons_layout)

        # Tabela de transações
        self.table = TransactionsTable()

        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    # Atualiza os valores do dashboard com base nas transações atuais
    def _update_dashboard(self):

        self.dashboard.update_values(
            self.finance.total_income(),
            self.finance.total_expenses(),
            self.finance.balance()
        )

    # Adiciona uma nova transação de renda
    def _add_income(self):

        dialog = TransactionDialog("Renda")

        if dialog.exec():

            data = dialog.get_data()

            transaction = Transaction(
                date=data["date"],
                description=data["description"],
                value=data["value"],
                category=data["category"],
                transaction_type=data["transaction_type"],
                payment_method=data["payment_method"]
            )

            self.finance.add_transaction(transaction)

            self._update_dashboard()

            self._update_table()

            self._update_charts()

    # Adiciona uma nova transação de despesa
    def _add_expense(self):

        dialog = TransactionDialog("Despesa")

        if dialog.exec():

            data = dialog.get_data()

            transaction = Transaction(
                date=data["date"],
                description=data["description"],
                value=data["value"],
                category=data["category"],
                transaction_type=data["transaction_type"],
                payment_method=data["payment_method"]
            )

            self.finance.add_transaction(transaction)

            self._update_dashboard()

            self._update_table()

            self._update_charts()

    def _update_table(self):
        self.table.load_transactions(
            self.finance.transactions
        )
        
    def _update_charts(self):

        self.charts.plot_expenses_by_category(
            self.finance.transactions
        )

        self.charts.plot_income_vs_expenses(
            self.finance.total_income(),
            self.finance.total_expenses()
        )