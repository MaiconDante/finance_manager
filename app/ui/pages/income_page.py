from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class IncomePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Rendas Page"))

        self.setLayout(layout)
