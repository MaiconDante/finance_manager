from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt

class ExpenseVariableTable(QTableWidget):

    def __init__(self):

        super().__init__()

        self._setup_table()


    def _setup_table(self):

        self.setColumnCount(6)


        self.setHorizontalHeaderLabels(
            [
                "Data",
                "Descrição",
                "Valor",
                "Categoria",
                "Pagamento",
                "Status"
            ]
        )


        # Todas as colunas mesmo tamanho

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )


        self.horizontalHeader().setVisible(True)


        # altura do cabeçalho
        # evita texto amassado

        self.horizontalHeader().setFixedHeight(50)


        header = self.horizontalHeader()


        header.setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        header.setMinimumSectionSize(
            100
        )


        self.verticalHeader().setVisible(False)


        self.setAlternatingRowColors(True)


        self.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )


        self.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )


        self.setEditTriggers(
            QTableWidget.NoEditTriggers
        )


        self.setFocusPolicy(
            Qt.NoFocus
        )


    def load_expenses(self, transactions):


        expenses = [

            t

            for t in transactions

            if t.transaction_type == "Despesa"

        ]


        self.setRowCount(
            len(expenses)
        )


        for row, expense in enumerate(expenses):


            item_date = QTableWidgetItem(
                expense.date.strftime("%d/%m/%Y")
            )


            item_description = QTableWidgetItem(
                expense.description
            )


            item_value = QTableWidgetItem(
                f"R$ {expense.value:.2f}"
            )


            item_category = QTableWidgetItem(
                expense.category
            )


            item_payment = QTableWidgetItem(
                expense.payment_method
            )


            item_status = QTableWidgetItem(
                getattr(
                    expense,
                    "status",
                    "Pendente"
                )
            )


            # centralizar conteúdo

            for item in [
                item_date,
                item_description,
                item_value,
                item_category,
                item_payment,
                item_status
            ]:

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )


            self.setItem(
                row,
                0,
                item_date
            )


            self.setItem(
                row,
                1,
                item_description
            )


            self.setItem(
                row,
                2,
                item_value
            )


            self.setItem(
                row,
                3,
                item_category
            )


            self.setItem(
                row,
                4,
                item_payment
            )


            self.setItem(
                row,
                5,
                item_status
            )
