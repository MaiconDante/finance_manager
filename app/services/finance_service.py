class FinanceService:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, value: float):
        self.incomes.append(value)

    def add_expense(self, value: float):
        self.expenses.append(value)

    def total_income(self):
        return sum(self.incomes)

    def total_expenses(self):
        return sum(self.expenses)

    def balance(self):
        return self.total_income() - self.total_expenses()
    