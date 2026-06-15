from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QStackedWidget, QMessageBox
)
from app.ui.navigation.navbar import Navbar

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.income_page import IncomePage
from app.ui.pages.expenses_variable_page import ExpensesVariablePage
from app.ui.pages.expenses_fixed_page import ExpensesFixedPage
from app.ui.pages.finance_settings_page import FinanceSettingsPage

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

        self.setWindowTitle("Finance System")

        self.finance = FinanceService()

        self._setup_ui()
        self._setup_pages()
        self._setup_connections()

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

    # Configura as páginas do sistema
    def _setup_pages(self):

        self.dashboard_page = DashboardPage()
        self.income_page = IncomePage()
        self.expenses_var_page = ExpensesVariablePage()
        self.expenses_fix_page = ExpensesFixedPage()
        self.settings_page = FinanceSettingsPage()

        self.stack.addWidget(self.dashboard_page)        # index 0
        self.stack.addWidget(self.income_page)           # index 1
        self.stack.addWidget(self.expenses_var_page)     # index 2
        self.stack.addWidget(self.expenses_fix_page)     # index 3
        self.stack.addWidget(self.settings_page)         # index 4

    # Configura o layout da janela principal
    def _setup_layout(self):

        main_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.navbar)
        layout.addWidget(self.stack)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    # Configura as conexões dos botões da navbar
    def _setup_connections(self):

        self.navbar.btn_dashboard.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        self.navbar.btn_income.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        self.navbar.btn_expenses_var.clicked.connect(
            lambda: self.stack.setCurrentIndex(2)
        )

        self.navbar.btn_expenses_fix.clicked.connect(
            lambda: self.stack.setCurrentIndex(3)
        )

        self.navbar.btn_settings.clicked.connect(
            lambda: self.stack.setCurrentIndex(4)
        )

    def _setup_ui(self):

        self.navbar = Navbar()
        self.stack = QStackedWidget()

        main_widget = QWidget()
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.navbar)
        self.layout.addWidget(self.stack)

        main_widget.setLayout(self.layout)

        self.setCentralWidget(main_widget)

    def _exit_app(self):

        resp = QMessageBox.question(
            self,
            "Sair",
            "Deseja realmente sair?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resp == QMessageBox.Yes:
            self.close()