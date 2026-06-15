from models.transaction import Transaction
class FinanceService:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def total_income(self):
        return sum(
            transaction.value
            for transaction in self.transactions
            if transaction.transaction_type == "Renda"
        )

    def total_expenses(self):
        return sum(
            transaction.value
            for transaction in self.transactions
            if transaction.transaction_type == "Despesa"
        )

    def balance(self):
        return self.total_income() - self.total_expenses()
    