from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Finance Manager")
        self.setMinimumSize(900, 600)
        #self.setWindowIcon(QIcon("./assets/images/app_icon.png"))

        # Initialize UI components
        self._init_ui()

    # Initialize the user interface
    def _init_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        
        # Create a vertical layout for the central widget
        layout = QVBoxLayout()

        # Add a title label to the layout
        title = QLabel("📊 Finance Manager - Dashboard Inicial")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Add the title label to the layout
        layout.addWidget(title)

        # Set the layout for the central widget and set it as the central widget of the main window
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
