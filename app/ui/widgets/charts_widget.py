from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout
)

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas
)

from matplotlib.figure import Figure

class ChartsWidget(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        layout = QHBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(10, 10, 10, 10)

        # gráfico pizza
        self.pie_figure = Figure()
        self.pie_canvas = FigureCanvas(
            self.pie_figure
        )

        # gráfico barras
        self.bar_figure = Figure()
        self.bar_canvas = FigureCanvas(
            self.bar_figure
        )

        self.pie_figure.tight_layout()
        self.bar_figure.tight_layout()

        layout.addWidget(self.pie_canvas)
        layout.addWidget(self.bar_canvas)

        self.setLayout(layout)

    def plot_expenses_by_category(
        self,
        transactions
    ):

        self.pie_figure.clear()

        ax = self.pie_figure.add_subplot(111)

        categories = {}

        for transaction in transactions:

            if transaction.transaction_type == "Despesa":

                categories[
                    transaction.category
                ] = (
                    categories.get(
                        transaction.category,
                        0
                    )
                    + transaction.value
                )

        if categories:

            ax.pie(
                list(categories.values()),
                labels=list(categories.keys()),
                autopct="%1.1f%%"
            )

        ax.set_title(
            "Despesas por Categoria"
        )

        self.pie_canvas.draw()

    def plot_income_vs_expenses(
        self,
        total_income,
        total_expenses
    ):

        self.bar_figure.clear()

        ax = self.bar_figure.add_subplot(111)

        ax.bar(
            ["Renda", "Despesas"],
            [total_income, total_expenses]
        )

        ax.set_title(
            "Renda vs Despesas"
        )

        self.bar_canvas.draw()
