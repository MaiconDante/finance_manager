from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)

class TransactionsTable(QTableWidget):

    def __init__(self):
        super().__init__()

        self._setup_table()

    def _setup_table(self):

        self.setColumnCount(5)

        self.setHorizontalHeaderLabels(
            [
                "Data",
                "Descrição",
                "Categoria",
                "Tipo",
                "Valor"
            ]
        )

        self.horizontalHeader().setStretchLastSection(True)

        self.setAlternatingRowColors(True)

    def load_transactions(self, transactions):

        self.setRowCount(len(transactions))

        for row, transaction in enumerate(transactions):

            self.setItem(
                row,
                0,
                QTableWidgetItem(
                    transaction.date.strftime("%d/%m/%Y")
                )
            )

            self.setItem(
                row,
                1,
                QTableWidgetItem(
                    transaction.description
                )
            )

            self.setItem(
                row,
                2,
                QTableWidgetItem(
                    transaction.category
                )
            )

            self.setItem(
                row,
                3,
                QTableWidgetItem(
                    transaction.transaction_type
                )
            )

            self.setItem(
                row,
                4,
                QTableWidgetItem(
                    f"R$ {transaction.value:.2f}"
                )
            )
