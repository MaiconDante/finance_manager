from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)
from PySide6.QtCore import Qt

class FinancialCard(QFrame):

    def __init__(self, title, card_type="default"):
        super().__init__()

        self.title = title
        self.card_type = card_type

        self._setup_ui()
        self._apply_style()

    def _setup_ui(self):

        self.setObjectName("financialCard")

        layout = QVBoxLayout()

        self.title_label = QLabel(self.title)
        self.value_label = QLabel("R$ 0,00")

        self.title_label.setObjectName("cardTitle")
        self.value_label.setObjectName("cardValue")

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)

        self.setLayout(layout)

    def update_value(self, value):

        self.value_label.setText(
            f"R$ {value:,.2f}"
        )

    def _apply_style(self):

        if self.card_type == "balance":
            self.setProperty("type", "balance")

        elif self.card_type == "income":
            self.setProperty("type", "income")

        elif self.card_type == "expense":
            self.setProperty("type", "expense")

        else:
            self.setProperty("type", "default")
