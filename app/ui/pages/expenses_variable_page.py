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

from datetime import date

from app.models.transaction import Transaction

from PySide6.QtCore import Qt, Signal

from app.ui.widgets.expense_variable_table import ExpenseVariableTable


class ExpensesVariablePage(QWidget):

    expense_created = Signal()


    def __init__(self, finance_service):

        super().__init__()

        self.finance = finance_service

        self.selected_expense = None

        self._setup_ui()



    def _setup_ui(self):

        main_layout = QVBoxLayout()


        title = QLabel(
            "💸 Despesas Variáveis"
        )

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)



        form_layout = QFormLayout()

        form_layout.setLabelAlignment(
            Qt.AlignLeft
        )

        form_layout.setHorizontalSpacing(30)

        form_layout.setVerticalSpacing(15)



        self.description_input = QLineEdit()

        self.description_input.setObjectName(
            "modernLineEdit"
        )



        self.value_input = QLineEdit()

        self.value_input.setObjectName(
            "modernLineEdit"
        )



        self.category_combo = QComboBox()

        self.category_combo.setObjectName(
            "modernCombo"
        )


        self.category_combo.addItems(
            [
                "Casa",
                "Alimentação",
                "Transporte",
                "Lazer",
                "Saúde",
                "Outros"
            ]
        )



        self.payment_combo = QComboBox()

        self.payment_combo.setObjectName(
            "modernCombo"
        )


        self.payment_combo.addItems(
            [
                "PIX",
                "Cartão",
                "Dinheiro",
                "Boleto",
                "Outros"
            ]
        )



        self.status_combo = QComboBox()

        self.status_combo.setObjectName(
            "modernCombo"
        )


        self.status_combo.addItems(
            [
                "Pendente",
                "Pago",
                "Cancelado"
            ]
        )



        form_layout.addRow(
            "Descrição:",
            self.description_input
        )


        form_layout.addRow(
            "Valor:",
            self.value_input
        )


        form_layout.addRow(
            "Categoria:",
            self.category_combo
        )


        form_layout.addRow(
            "Pagamento:",
            self.payment_combo
        )


        form_layout.addRow(
            "Situação:",
            self.status_combo
        )



        container = QWidget()

        container.setObjectName(
            "formContainer"
        )

        container.setLayout(
            form_layout
        )


        main_layout.addWidget(container)



        # =====================
        # BOTÕES
        # =====================

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



        self.table = ExpenseVariableTable()


        main_layout.addWidget(
            self.table
        )


        self.setLayout(
            main_layout
        )

        self.save_button.clicked.connect(
            self._save_expense
        )

        self.edit_button.clicked.connect(
            self._edit_expense
        )

        self.delete_button.clicked.connect(
            self._delete_expense
        )

        self.clear_button.clicked.connect(
            self._clear_form
        )


        self.table.cellClicked.connect(
            self._select_expense
        )


        self.table.load_expenses(
            self.finance.transactions
        )



    def _save_expense(self):


        if not self._validate_form():

            return



        if self.selected_expense:


            self.selected_expense.description = (
                self.description_input.text()
            )


            self.selected_expense.value = float(
                self.value_input.text()
            )


            self.selected_expense.category = (
                self.category_combo.currentText()
            )


            self.selected_expense.payment_method = (
                self.payment_combo.currentText()
            )


            self.selected_expense.status = (
                self.status_combo.currentText()
            )


            self.finance.update_transaction(
                self.selected_expense
            )



        else:


            expense = Transaction(

                date=date.today(),

                description=self.description_input.text(),

                value=float(
                    self.value_input.text()
                ),

                category=self.category_combo.currentText(),

                transaction_type="Despesa",

                payment_method=self.payment_combo.currentText(),

                status=self.status_combo.currentText()

            )


            self.finance.add_transaction(
                expense
            )



        self.table.load_expenses(
            self.finance.transactions
        )


        self.expense_created.emit()


        self._clear_form()




    def _select_expense(self, row, column):


        expenses = [

            t for t in self.finance.transactions

            if t.transaction_type == "Despesa"

        ]


        if row < len(expenses):

            self.selected_expense = expenses[row]


            self.edit_button.setEnabled(True)

            self.delete_button.setEnabled(True)




    def _edit_expense(self):


        if not self.selected_expense:


            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma despesa."
            )

            return



        self.description_input.setText(
            self.selected_expense.description
        )


        self.value_input.setText(
            str(self.selected_expense.value)
        )


        self.category_combo.setCurrentText(
            self.selected_expense.category
        )


        self.payment_combo.setCurrentText(
            self.selected_expense.payment_method
        )


        self.status_combo.setCurrentText(
            self.selected_expense.status
        )


        self.save_button.setText(
            "Atualizar"
        )



    def _delete_expense(self):


        if not self.selected_expense:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma despesa."
            )

            return



        confirm = QMessageBox.question(
            self,
            "Excluir",
            "Deseja excluir essa despesa?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirm == QMessageBox.Yes:


            self.finance.delete_transaction(
                self.selected_expense
            )


            self.table.load_expenses(
                self.finance.transactions
            )


            self.expense_created.emit()


            self._clear_form()




    def _clear_form(self):


        self.description_input.clear()

        self.value_input.clear()

        self.category_combo.setCurrentIndex(0)

        self.payment_combo.setCurrentIndex(0)

        self.status_combo.setCurrentIndex(0)



        self.selected_expense = None


        self.table.clearSelection()


        self.save_button.setText(
            "Salvar"
        )



    def _validate_form(self):


        if not self.description_input.text().strip():

            QMessageBox.warning(
                self,
                "Atenção",
                "Informe uma descrição."
            )

            return False



        try:

            value = float(
                self.value_input.text()
            )


        except ValueError:


            QMessageBox.warning(
                self,
                "Atenção",
                "Digite um valor válido."
            )

            return False



        if value <= 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Valor deve ser maior que zero."
            )

            return False



        return True
    