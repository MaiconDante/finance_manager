from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QComboBox
)

from datetime import date
from app.models.transaction import Transaction
from app.ui.widgets.income_table import IncomeTable

class IncomePage(QWidget):

    def __init__(self, finance_service):

        super().__init__()

        self.finance = finance_service

        self._setup_ui()


    def _setup_ui(self):

        main_layout = QVBoxLayout()


        # ==========================
        # TITULO
        # ==========================

        title = QLabel("💰 Rendas")

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)


        # ==========================
        # FORMULARIO
        # ==========================

        form_layout = QFormLayout()

        self.income_type_combo = QComboBox()

        self.income_type_combo.addItems(
            [
                "Salário",
                "Extra",
                "Saldo Restante Anterior",
                "Décimo Terceiro",
                "PIS/PASEP",
                "Outros"
            ]
        )

        self.value_input = QLineEdit()

        form_layout.addRow(
            "Tipo de Renda:",
            self.income_type_combo
        )

        form_layout.addRow(
            "Valor:",
            self.value_input
        )

        self.payment_combo = QComboBox()

        self.payment_combo.addItems(
            [
                "PIX",
                "Cartão de Crédito",
                "Dinheiro",
                "Outros"
            ]
        )

        form_layout.addRow(
            "Forma de Pagamento:",
            self.payment_combo
        )

        main_layout.addLayout(
            form_layout
        )

        # ==========================
        # BOTOES
        # ==========================

        buttons_layout = QHBoxLayout()

        self.save_button = QPushButton(
            "Salvar"
        )

        self.cancel_button = QPushButton(
            "Cancelar"
        )

        buttons_layout.addWidget(
            self.save_button
        )

        buttons_layout.addWidget(
            self.cancel_button
        )

        main_layout.addLayout(
            buttons_layout
        )

        self.table = IncomeTable()

        main_layout.addWidget(
            self.table
        )

        self.setLayout(
            main_layout
        )

        self.save_button.clicked.connect(
            self._save_income
        )

        self.cancel_button.clicked.connect(
            self._clear_form
        )

    def _save_income(self):

        transaction = Transaction(

            date=date.today(),

            description=self.income_type_combo.currentText(),

            value=float(
                self.value_input.text()
            ),

            category="Renda",

            transaction_type="Renda",

            payment_method=self.payment_combo.currentText()
        )


        self.finance.add_transaction(
            transaction
        )

        self.table.load_income(
            self.finance.transactions
        )

        self._clear_form()

    def _clear_form(self):

        self.income_type_combo.setCurrentIndex(0)

        self.value_input.clear()

        self.payment_combo.setCurrentIndex(0)