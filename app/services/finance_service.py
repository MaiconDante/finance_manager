from app.models.transaction import Transaction
from app.database import repository

class FinanceService:

    def __init__(self):
        repository.create_table()
        self.transactions = repository.get_all_transactions()

    def add_transaction(self, transaction):
        repository.insert_transaction(transaction)
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
    