from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

class FinancialCard(QFrame):

    def __init__(self, title):
        super().__init__()

        self.title = title

        self._setup_ui()

    def _setup_ui(self):

        self.setFrameShape(QFrame.Shape.StyledPanel)

        layout = QVBoxLayout()

        self.title_label = QLabel(self.title)
        self.value_label = QLabel("R$ 0,00")

        self.title_label.setStyleSheet(
            """
            font-size: 14px;
            font-weight: bold;
            """
        )

        self.value_label.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            """
        )

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)

        self.setLayout(layout)

    def update_value(self, value):

        self.value_label.setText(
            f"R$ {value:.2f}"
        )
