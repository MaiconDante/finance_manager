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

from math import ceil

from PySide6.QtCore import Signal, Qt
from datetime import date

from app.models.transaction import Transaction
from app.ui.widgets.income_table import IncomeTable


class IncomePage(QWidget):

    income_created = Signal()


    def __init__(self, finance_service):

        super().__init__()

        self.current_page = 1

        self.items_per_page = 6

        self.all_incomes = []

        self.finance = finance_service

        self.selected_income = None

        self.editing_mode = False

        self._setup_ui()


    def _setup_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel("💰 Rendas")

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)


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

        self.income_type_combo.setMinimumWidth(
            350
        )


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

        self.value_input.setObjectName(
            "modernLineEdit"
        )

        self.value_input.setMinimumWidth(
            350
        )



        self.payment_combo = QComboBox()

        self.payment_combo.setObjectName(
            "modernCombo"
        )

        self.payment_combo.setMinimumWidth(
            350
        )


        self.payment_combo.addItems(
            [
                "PIX",
                "Cartão de Crédito",
                "Dinheiro",
                "Outros"
            ]
        )


        form_layout.addRow(
            "Tipo de Renda:",
            self.income_type_combo
        )


        form_layout.addRow(
            "Valor:",
            self.value_input
        )


        form_layout.addRow(
            "Forma de Pagamento:",
            self.payment_combo
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

        self.save_button.setText(
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

        # ==========================
        # PESQUISA
        # ==========================

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Pesquisar renda..."
        )

        self.search_input.setObjectName(
            "modernLineEdit"
        )

        main_layout.addWidget(
            self.search_input
        )

        self.table = IncomeTable()


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


        self._load_page()

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


        self.clear_button.clicked.connect(
            self._clear_form
        )

        self.search_input.textChanged.connect(
            self._filter_incomes
        )

        self.previous_button.clicked.connect(
            self._previous_page
        )

        self.next_button.clicked.connect(
            self._next_page
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


            QMessageBox.information(
                self,
                "Sucesso",
                "Renda atualizada com sucesso."
            )


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


            QMessageBox.information(
                self,
                "Sucesso",
                "Renda cadastrada com sucesso."
            )



        self.table.load_income(
            self.finance.transactions
        )


        self.income_created.emit()


        self._clear_form()

        self.save_button.setText(
            "Salvar"
        )

        self.editing_mode = False


    def _select_income(self, row, column):

        incomes = [

            t for t in self.finance.transactions

            if t.transaction_type == "Renda"

        ]

        if row < len(incomes):

            self.selected_income = incomes[row]


    def _edit_income(self):

        selected = self.table.selectedItems()

        if not selected:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma renda para editar."
            )

            return

        row = self.table.currentRow()

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

        self.save_button.setText(
            "Atualizar"
        )

        self.editing_mode = True


    def _delete_income(self):


        if not self.table.selectedItems():


            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma renda para excluir."
            )


            return



        row = self.table.currentRow()



        confirm = QMessageBox.question(

            self,
            "Excluir",

            "Deseja realmente excluir esta renda?",

            QMessageBox.Yes |
            QMessageBox.No

        )



        if confirm == QMessageBox.Yes:


            incomes = [

                t for t in self.finance.transactions

                if t.transaction_type == "Renda"

            ]


            income = incomes[row]


            self.finance.delete_transaction(
                income
            )


            self.table.load_income(
                self.finance.transactions
            )


            self.income_created.emit()


            QMessageBox.information(
                self,
                "Sucesso",
                "Renda excluída com sucesso."
            )


            self._clear_form()



    def _clear_form(self):


        self.income_type_combo.setCurrentIndex(0)

        self.value_input.clear()

        self.payment_combo.setCurrentIndex(0)


        self.selected_income = None


        self.table.clearSelection()

        self.save_button.setText(
            "Salvar"
        )


        self.editing_mode = False

        self.table.setCurrentCell(-1,-1)


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
                "Digite um valor válido."
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
    
    
    def _filter_incomes(self):

        text = self.search_input.text().lower()

        incomes = [

            t for t in self.finance.transactions

            if t.transaction_type == "Renda"

            and (
                text in t.description.lower()
                or text in t.payment_method.lower()
            )
        ]

        self.table.load_income(
            incomes
        )


    def _load_page(self):

        self.all_incomes = [

            t for t in self.finance.transactions

            if t.transaction_type == "Renda"

        ]


        total_pages = max(
            1,
            ceil(
                len(self.all_incomes) /
                self.items_per_page
            )
        )


        if self.current_page > total_pages:

            self.current_page = total_pages



        start = (
            self.current_page - 1
        ) * self.items_per_page


        end = start + self.items_per_page



        page_items = self.all_incomes[start:end]



        self.table.load_income(
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


    def _next_page(self):

        self.current_page += 1

        self._load_page()


    def _previous_page(self):

        self.current_page -= 1

        self._load_page()
