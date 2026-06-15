from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QDateEdit, 
    QMessageBox
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

        self.save_button.clicked.connect(self._save)

    def get_data(self):
        return {
            "date": self.date_edit.date().toPython(),
            "description": self.description_edit.text(),
            "value": float(self.value_edit.text()),
            "category": self.category_combo.currentText(),
            "payment_method": self.payment_combo.currentText(),
            "transaction_type": self.transaction_type
        }

    def _validate_fields(self):

        description = self.description_edit.text().strip()
        value = self.value_edit.text().strip()

        if not description:
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe uma descrição."
            )
            return False

        if not value:
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe um valor."
            )
            return False

        try:
            float(value)
        except ValueError:
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe um valor numérico válido."
            )
            return False
        
        value = float(value)

        if value <= 0:
            QMessageBox.warning(
                self,
                "Atenção",
                "O valor deve ser maior que zero."
            )
            return False

        return True
    
    def _save(self):

        if self._validate_fields():
            self.accept()