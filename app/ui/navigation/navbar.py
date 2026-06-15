from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class Navbar(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout()

        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_income = QPushButton("Rendas")
        self.btn_expenses_var = QPushButton("Despesas Variáveis")
        self.btn_expenses_fix = QPushButton("Despesas Fixas")
        self.btn_settings = QPushButton("Cadastros Financeiros")
        self.btn_exit = QPushButton("Sair")

        layout.addWidget(self.btn_dashboard)
        layout.addWidget(self.btn_income)
        layout.addWidget(self.btn_expenses_var)
        layout.addWidget(self.btn_expenses_fix)
        layout.addWidget(self.btn_settings)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)
