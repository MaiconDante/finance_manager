from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)


class IncomeTable(QTableWidget):

    def __init__(self):

        super().__init__()

        self._setup_table()


    def _setup_table(self):

        self.setColumnCount(4)

        self.setHorizontalHeaderLabels(
            [
                "Data",
                "Tipo",
                "Valor",
                "Forma de Pagamento"
            ]
        )


        self.horizontalHeader().setStretchLastSection(
            True
        )


    def load_income(self, transactions):

        incomes = [

            t for t in transactions

            if t.transaction_type == "Renda"

        ]


        self.setRowCount(
            len(incomes)
        )


        for row, income in enumerate(incomes):

            self.setItem(
                row,
                0,
                QTableWidgetItem(
                    income.date.strftime("%d/%m/%Y")
                )
            )


            self.setItem(
                row,
                1,
                QTableWidgetItem(
                    income.description
                )
            )


            self.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"R$ {income.value:.2f}"
                )
            )


            self.setItem(
                row,
                3,
                QTableWidgetItem(income.payment_method)
            )
