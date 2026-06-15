from app.models.transaction import Transaction
from app.database import repository
from app.services.insights_service import InsightsService

class FinanceService:

    def __init__(self):
        repository.create_table()
        self.transactions = repository.get_all_transactions()
        self.insights_service = InsightsService()

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
    
    def get_insights(self):

        return self.insights_service.analyze(
            self.transactions,
            self.total_income(),
            self.total_expenses()
        )
    