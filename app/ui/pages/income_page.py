from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QComboBox,
    QMessageBox
)
from PySide6.QtCore import Signal, Qt
from datetime import date
from app.models.transaction import Transaction
from app.ui.widgets.income_table import IncomeTable

class IncomePage(QWidget):

    income_created = Signal()

    def __init__(self, finance_service):

        super().__init__()

        self.finance = finance_service

        self.selected_income = None

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

        form_layout.setLabelAlignment(
            Qt.AlignLeft
        )

        form_layout.setHorizontalSpacing(
            30
        )

        form_layout.setVerticalSpacing(
            15
        )

        self.income_type_combo = QComboBox()

        self.income_type_combo.setObjectName(
            "modernCombo"
        )
        self.income_type_combo.setMinimumWidth(350)

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

        self.value_input.setMinimumWidth(350)

        form_layout.addRow(
            "Tipo de Renda:",
            self.income_type_combo
        )

        form_layout.addRow(
            "Valor:",
            self.value_input
        )

        self.payment_combo = QComboBox()

        self.payment_combo.setObjectName(
            "modernCombo"
        )

        self.value_input.setEnabled(False)

        self.income_type_combo.setEnabled(False)

        self.payment_combo.setEnabled(False)

        self.value_input.setObjectName(
            "modernLineEdit"
        )

        self.payment_combo.setMinimumWidth(350)

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

        container = QWidget()
        container.setObjectName("formContainer")

        container.setLayout(form_layout)

        main_layout.addWidget(container)

        # ==========================
        # BOTOES
        # ==========================

        buttons_layout = QHBoxLayout()

        self.save_button = QPushButton(
            "Salvar"
        )

        self.save_button.setObjectName(
            "saveButton"
        )

        self.edit_button = QPushButton(
            "Editar"
        )

        self.edit_button.setObjectName(
            "editButton"
        )

        self.delete_button = QPushButton(
            "Excluir"
        )

        self.delete_button.setObjectName(
            "deleteButton"
        )


        self.clear_button = QPushButton(
            "Limpar"
        )

        self.clear_button.setObjectName(
            "clearButton"
        )

        buttons_layout.addWidget(
            self.save_button
        )

        buttons_layout.addWidget(
            self.edit_button
        )

        buttons_layout.addWidget(
            self.delete_button
        )

        buttons_layout.addWidget(
            self.clear_button
        )

        main_layout.addLayout(
            buttons_layout
        )

        self.table = IncomeTable()

        main_layout.addWidget(
            self.table
        )

        self.table.load_income(
            self.finance.transactions
        )

        self.setLayout(
            main_layout
        )

        self.save_button.clicked.connect(
            self._save_income
        )

        self.edit_button.clicked.connect(
            self._edit_income
        )

        self.delete_button.clicked.connect(
            self._delete_income
        )

        self.table.cellClicked.connect(
            self._select_income
        )

        self.clear_button.clicked.connect(
            self._clear_form
        )

    def _save_income(self):

        if not self._validate_form():

            return

        if self.selected_income:

            self.selected_income.description = (
                self.income_type_combo.currentText()
            )


            self.selected_income.value = float(
                self.value_input.text()
            )


            self.selected_income.payment_method = (
                self.payment_combo.currentText()
            )


            self.finance.update_transaction(
                self.selected_income
            )


            self.selected_income = None


        else:

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

        self.income_created.emit()

        self._clear_form()

        self.income_type_combo.setEnabled(False)

        self.value_input.setEnabled(False)

        self.payment_combo.setEnabled(False)


    def _select_income(self, row, column):

        incomes = [

            t for t in self.finance.transactions

            if t.transaction_type == "Renda"

        ]


        if row < len(incomes):

            self.selected_income = incomes[row]


            self.income_type_combo.setCurrentText(
                self.selected_income.description
            )


            self.value_input.setText(
                str(self.selected_income.value)
            )


            self.payment_combo.setCurrentText(
                self.selected_income.payment_method
            )


    def _delete_income(self):

        row = self.table.currentRow()


        if row < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma renda para excluir."
            )

            return


        confirm = QMessageBox.question(
            self,
            "Excluir",
            "Deseja realmente excluir essa renda?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirm == QMessageBox.Yes:

            income = [
                t for t in self.finance.transactions
                if t.transaction_type == "Renda"
            ][row]


            self.finance.delete_transaction(
                income
            )


            self.table.load_income(
                self.finance.transactions
            )

            self.income_created.emit()

    def _clear_form(self):

        self.income_type_combo.setCurrentIndex(0)

        self.value_input.clear()

        self.payment_combo.setCurrentIndex(0)

    def _validate_form(self):

        value = self.value_input.text().strip()


        if not value:

            QMessageBox.warning(
                self,
                "Atenção",
                "Informe um valor."
            )

            return False


        try:

            value = float(value)


        except ValueError:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite um valor numérico válido."
            )

            return False



        if value <= 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "O valor deve ser maior que zero."
            )

            return False


        return True
    

    def _edit_income(self):

        row = self.table.currentRow()


        if row < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma renda."
            )

            return


        incomes = [

            t for t in self.finance.transactions

            if t.transaction_type == "Renda"

        ]


        self.selected_income = incomes[row]


        self.income_type_combo.setCurrentText(
            self.selected_income.description
        )


        self.value_input.setText(
            str(self.selected_income.value)
        )


        self.payment_combo.setCurrentText(
            self.selected_income.payment_method
        )


        # libera edição

        self.income_type_combo.setEnabled(True)

        self.value_input.setEnabled(True)

        self.payment_combo.setEnabled(True)