from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QDateEdit
)

from PySide6.QtCore import QDate

class TransactionDialog(QDialog):

    def __init__(self, transaction_type):
        super().__init__()

        self.transaction_type = transaction_type

        self.setWindowTitle(f"Nova {transaction_type}")

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        form = QFormLayout()

        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)

        self.description_edit = QLineEdit()

        self.value_edit = QLineEdit()

        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "Alimentação",
            "Moradia",
            "Transporte",
            "Saúde",
            "Lazer",
            "Tecnologia",
            "Educação",
            "Outros"
        ])

        self.payment_combo = QComboBox()
        self.payment_combo.addItems([
            "PIX",
            "Cartão",
            "Dinheiro",
            "Boleto"
        ])

        form.addRow("Data:", self.date_edit)
        form.addRow("Descrição:", self.description_edit)
        form.addRow("Valor:", self.value_edit)
        form.addRow("Categoria:", self.category_combo)
        form.addRow("Pagamento:", self.payment_combo)

        self.save_button = QPushButton("Salvar")

        layout.addLayout(form)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.save_button.clicked.connect(self.accept)

    def get_data(self):
        return {
            "date": self.date_edit.date().toPython(),
            "description": self.description_edit.text(),
            "value": float(self.value_edit.text()),
            "category": self.category_combo.currentText(),
            "payment_method": self.payment_combo.currentText(),
            "transaction_type": self.transaction_type
        }
