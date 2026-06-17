from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)
from PySide6.QtCore import Qt


class IncomeTable(QTableWidget):

    def __init__(self):

        super().__init__()

        self._setup_table()

    def _setup_table(self):

        self.setColumnCount(4)

        self.setHorizontalHeaderLabels(
            [
                "Data",
                "Tipo de Renda",
                "Valor",
                "Forma de Pagamento"
            ]
        )

        # Todas as colunas com mesmo tamanho
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.horizontalHeader().setVisible(True)

        self.horizontalHeader().setFixedHeight(50)

        header = self.horizontalHeader()

        header.setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        header.setMinimumSectionSize(100)

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

    def load_income(self, transactions):

        incomes = [
            t
            for t in transactions
            if t.transaction_type == "Renda"
        ]

        self.setRowCount(
            len(incomes)
        )

        for row, income in enumerate(incomes):

            item_date = QTableWidgetItem(
                income.date.strftime("%d/%m/%Y")
            )

            item_type = QTableWidgetItem(
                income.description
            )

            item_value = QTableWidgetItem(
                f"R$ {income.value:.2f}"
            )

            item_payment = QTableWidgetItem(
                income.payment_method
            )

            # Centralizar conteúdo
            item_date.setTextAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            item_type.setTextAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            item_value.setTextAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            item_payment.setTextAlignment(
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
                item_type
            )

            self.setItem(
                row,
                2,
                item_value
            )

            self.setItem(
                row,
                3,
                item_payment
            )
