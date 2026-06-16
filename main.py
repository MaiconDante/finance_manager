import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from PySide6.QtCore import QFile, QTextStream

def load_styles(app):
    file = QFile("app/styles/theme.qss")

    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())

def main():
    app = QApplication([])
    load_styles(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
