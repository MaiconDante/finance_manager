from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QMessageBox
)

from app.services.finance_service import FinanceService

from app.ui.navigation.navbar import Navbar

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.income_page import IncomePage
from app.ui.pages.expenses_variable_page import ExpensesVariablePage
from app.ui.pages.expenses_fixed_page import ExpensesFixedPage
from app.ui.pages.finance_settings_page import FinanceSettingsPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance System")
        self.resize(1200, 800)

        self.finance = FinanceService()

        self._setup_ui()
        self._setup_pages()
        self._setup_connections()

    def _setup_ui(self):

        self.navbar = Navbar()
        self.stack = QStackedWidget()

        main_widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.navbar)
        layout.addWidget(self.stack)

        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

    def _setup_pages(self):

        self.dashboard_page = DashboardPage(
            self.finance
        )


        self.income_page = IncomePage(
            self.finance
        )


        self.expenses_var_page = ExpensesVariablePage(
            self.finance
        )


        self.expenses_fix_page = ExpensesFixedPage(
            self.finance
        )

        self.settings_page = FinanceSettingsPage(
            self.finance
        )

        self.stack.addWidget(self.dashboard_page)      # index 0
        self.stack.addWidget(self.income_page)         # index 1
        self.stack.addWidget(self.expenses_var_page)   # index 2
        self.stack.addWidget(self.expenses_fix_page)   # index 3
        self.stack.addWidget(self.settings_page)       # index 4

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

        self.navbar.btn_exit.clicked.connect(
            self._exit_app
        )

        self.income_page.income_created.connect(
            self._refresh_dashboard
        )

        self.expenses_var_page.expense_created.connect(
            self._refresh_dashboard
        )

    def _exit_app(self):

        resp = QMessageBox.question(
            self,
            "Sair",
            "Deseja realmente sair?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resp == QMessageBox.Yes:
            self.close()

    def _refresh_dashboard(self):

     self.dashboard_page.refresh()
            