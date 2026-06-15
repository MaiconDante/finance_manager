from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem
)

from app.services.finance_service import FinanceService
from app.ui.transaction_dialog import TransactionDialog
from app.models.transaction import Transaction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance Manager")
        self.setMinimumSize(900, 600)

        # serviço central do sistema
        self.finance = FinanceService()

        self._init_ui()
        self._update_dashboard()

    def _init_ui(self):
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Título
        self.title = QLabel("📊 Dashboard Financeiro")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.title)

        # Labels do dashboard
        self.label_income = QLabel()
        self.label_expenses = QLabel()
        self.label_balance = QLabel()

        self.layout.addWidget(self.label_income)
        self.layout.addWidget(self.label_expenses)
        self.layout.addWidget(self.label_balance)

        # Botões
        buttons_layout = QHBoxLayout()

        btn_income = QPushButton("Adicionar Renda")
        btn_expense = QPushButton("Adicionar Despesa")

        btn_income.clicked.connect(self._add_income)
        btn_expense.clicked.connect(self._add_expense)

        buttons_layout.addWidget(btn_income)
        buttons_layout.addWidget(btn_expense)

        self.layout.addLayout(buttons_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Data", "Descrição", "Valor", "Categoria", "Tipo"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)

        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def _update_dashboard(self):
        self.label_income.setText(f"💰 Renda total: R$ {self.finance.total_income():.2f}")
        self.label_expenses.setText(f"💸 Despesas total: R$ {self.finance.total_expenses():.2f}")
        self.label_balance.setText(f"💵 Saldo: R$ {self.finance.balance():.2f}")

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

    def _update_table(self):

        transactions = self.finance.transactions

        self.table.setRowCount(len(transactions))

        for row, transaction in enumerate(transactions):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    transaction.date.strftime("%d/%m/%Y")
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    transaction.description
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    transaction.category
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    transaction.transaction_type
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    f"R$ {transaction.value:.2f}"
                )
            )
