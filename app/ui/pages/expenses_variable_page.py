from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QComboBox,
    QMessageBox,
    QGridLayout
)

from math import ceil

from datetime import date

from app.models.transaction import Transaction

from PySide6.QtCore import Qt, Signal

from app.ui.widgets.expense_variable_table import ExpenseVariableTable



class ExpensesVariablePage(QWidget):

    expense_created = Signal()


    def __init__(self, finance_service):

        super().__init__()

        self.finance = finance_service

        self.current_page = 1

        self.items_per_page = 6

        self.all_expenses = []

        self.selected_expense = None

        self.editing_mode = False

        self._setup_ui()



    def _setup_ui(self):

        main_layout = QVBoxLayout()


        title = QLabel(
            "💸 Despesas Variáveis"
        )

        title.setObjectName(
            "pageTitle"
        )


        main_layout.addWidget(
            title
        )



        form_layout = QGridLayout()


        form_layout.setHorizontalSpacing(
            30
        )

        form_layout.setVerticalSpacing(
            15
        )



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



        form_layout.addWidget(
            QLabel("Descrição:"),
            0,
            0
        )

        form_layout.addWidget(
            self.description_input,
            0,
            1
        )


        form_layout.addWidget(
            QLabel("Valor:"),
            0,
            2
        )

        form_layout.addWidget(
            self.value_input,
            0,
            3
        )



        form_layout.addWidget(
            QLabel("Categoria:"),
            1,
            0
        )


        form_layout.addWidget(
            self.category_combo,
            1,
            1
        )



        form_layout.addWidget(
            QLabel("Pagamento:"),
            1,
            2
        )


        form_layout.addWidget(
            self.payment_combo,
            1,
            3
        )



        form_layout.addWidget(
            QLabel("Situação:"),
            2,
            0
        )


        form_layout.addWidget(
            self.status_combo,
            2,
            1
        )



        container = QWidget()

        container.setObjectName(
            "formContainer"
        )

        container.setLayout(
            form_layout
        )


        main_layout.addWidget(
            container
        )



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

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Pesquisar despesa..."
        )

        self.search_input.setObjectName(
            "modernLineEdit"
        )

        self.search_input.setMinimumWidth(
            350
        )

        main_layout.addWidget(
            self.search_input
        )

        self.table = ExpenseVariableTable()


        main_layout.addWidget(
            self.table
        )

        self.pagination_layout = QHBoxLayout()


        self.previous_button = QPushButton(
            "◀ Anterior"
        )


        self.page_label = QLabel(
            "Página 1 de 1"
        )


        self.next_button = QPushButton(
            "Próxima ▶"
        )


        self.pagination_layout.addWidget(
            self.previous_button
        )

        self.pagination_layout.addWidget(
            self.page_label
        )

        self.pagination_layout.addWidget(
            self.next_button
        )


        main_layout.addLayout(
            self.pagination_layout
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


        self.previous_button.clicked.connect(
            self._previous_page
        )


        self.next_button.clicked.connect(
            self._next_page
        )

        self.search_input.textChanged.connect(
            self._filter_expenses
        )


        self._load_page()



    def _load_page(self):


        self.all_expenses = [

            t for t in self.finance.transactions

            if t.transaction_type == "Despesa"

        ]


        total_pages = max(

            1,

            ceil(

                len(self.all_expenses)

                /

                self.items_per_page

            )

        )



        if self.current_page > total_pages:

            self.current_page = total_pages



        start = (

            self.current_page - 1

        ) * self.items_per_page



        end = start + self.items_per_page



        page_items = self.all_expenses[start:end]



        self.table.load_expenses(
            page_items
        )



        self.page_label.setText(

            f"Página {self.current_page} de {total_pages}"

        )


        self.previous_button.setEnabled(

            self.current_page > 1

        )


        self.next_button.setEnabled(

            self.current_page < total_pages

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



        self.expense_created.emit()


        self._clear_form()


        self._load_page()

        self.expense_created.emit()

        self._clear_form()



    def _select_expense(self,row,column):


        index = (

            (self.current_page - 1)

            *

            self.items_per_page

            +

            row

        )


        if index < len(self.all_expenses):


            self.selected_expense = self.all_expenses[index]




    def _edit_expense(self):


        if not self.selected_expense:


            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma despesa para editar."
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


        self.editing_mode = True




    def _delete_expense(self):


        if not self.selected_expense:


            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma despesa para excluir."
            )

            return



        confirm = QMessageBox.question(

            self,
            "Excluir",

            "Deseja excluir essa despesa?",

            QMessageBox.Yes |

            QMessageBox.No

        )



        if confirm == QMessageBox.Yes:


            self.finance.delete_transaction(
                self.selected_expense
            )


            self.expense_created.emit()


            self._load_page()

            self._clear_form()




    def _clear_form(self):


        self.description_input.clear()


        self.value_input.clear()


        self.category_combo.setCurrentIndex(0)


        self.payment_combo.setCurrentIndex(0)


        self.status_combo.setCurrentIndex(0)



        self.selected_expense = None


        self.editing_mode = False


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




    def _next_page(self):

        self.current_page += 1

        self._load_page()




    def _previous_page(self):

        self.current_page -= 1

        self._load_page()



    def _filter_expenses(self):


        text = self.search_input.text().lower()



        self.all_expenses = [

            t for t in self.finance.transactions

            if t.transaction_type == "Despesa"

            and (

                text in t.description.lower()

                or text in t.category.lower()

                or text in t.status.lower()

                or text in t.payment_method.lower()

                or text in str(t.date).lower()

            )

        ]



        self.current_page = 1


        self._load_page()