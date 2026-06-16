from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class IncomePage(QWidget):

    def __init__(self, finance_service):
        super().__init__()

        self.finance = finance_service
        
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Rendas Page"))

        self.setLayout(layout)
