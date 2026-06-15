from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartsWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

    def plot_expenses_by_category(self, transactions):

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        categories = {}
        
        for t in transactions:
            if t.transaction_type == "Despesa":
                categories[t.category] = categories.get(t.category, 0) + t.value

        labels = list(categories.keys())
        values = list(categories.values())

        ax.pie(values, labels=labels, autopct="%1.1f%%")

        ax.set_title("Despesas por Categoria")

        self.canvas.draw()

    def plot_income_vs_expenses(self, total_income, total_expenses):

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        labels = ["Renda", "Despesas"]
        values = [total_income, total_expenses]

        ax.bar(labels, values)

        ax.set_title("Renda vs Despesas")

        self.canvas.draw()
