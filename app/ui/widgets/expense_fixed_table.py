from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt


class ExpenseFixedTable(QTableWidget):

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


        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.horizontalHeader().setFixedHeight(50)


        self.verticalHeader().setVisible(False)


        self.setSelectionBehavior(
            QTableWidget.SelectRows
        )


        self.setEditTriggers(
            QTableWidget.NoEditTriggers
        )


    def load_expenses(self, transactions):


        expenses = [

            t

            for t in transactions

            if t.transaction_type == "Despesa Fixa"

        ]


        self.setRowCount(
            len(expenses)
        )


        for row, expense in enumerate(expenses):


            values = [

                expense.date.strftime("%d/%m/%Y"),

                expense.description,

                f"R$ {expense.value:.2f}",

                expense.category,

                expense.payment_method,

                expense.status

            ]


            for column, value in enumerate(values):


                item = QTableWidgetItem(
                    str(value)
                )


                item.setTextAlignment(
                    Qt.AlignCenter
                )


                self.setItem(
                    row,
                    column,
                    item
                )
                