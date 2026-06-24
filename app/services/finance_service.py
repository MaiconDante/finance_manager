from app.database import repository
from app.services.insights_engine import InsightsEngine

class FinanceService:

    def __init__(self):
        repository.create_table()
        self.transactions = repository.get_all_transactions()
        self.insights_engine = InsightsEngine()

        # Categorias

        self.categories = [
            "Moradia",
            "Alimentação",
            "Transporte",
            "Lazer",
            "Saúde",
            "Serviços",
            "Assinaturas",
            "Entretenimento",
            "Tecnologia",
            "Jogos",
            "Outros"
        ]


        # Formas de pagamento

        self.payment_methods = [
            "PIX",
            "Cartão de Crédito",
            "Dinheiro",
            "Boleto",
            "Débito",
            "Outros"
        ]


        # Status

        self.status_list = [
            "Pendente",
            "Pago",
            "Cancelado"
        ]


        # Tipos de renda

        self.income_types = [
            "Salário",
            "Freelance",
            "Investimento",
            "Décimo Terceiro",
            "PIS/PASEP",
            "Outros"
        ]

    def add_transaction(self, transaction):
        repository.insert_transaction(transaction)
        self.transactions.append(transaction)

    def update_transaction(self, transaction):

        repository.update_transaction(
            transaction
        )

        for index, item in enumerate(self.transactions):

            if item.id == transaction.id:

                self.transactions[index] = transaction

                break

    def delete_transaction(self, transaction):
        repository.delete_transaction(transaction)
        self.transactions.remove(transaction)

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

        return self.insights_engine.analyze(
            self.transactions,
            self.total_income(),
            self.total_expenses()
        )
    
    def add_category(self, category):

        category = category.strip()

        if not category:
            return False

        if category.lower() in [
            item.lower()
            for item in self.categories
        ]:
            return False

        self.categories.append(category)

        return True
    
    def remove_category(self, category):

        if category not in self.categories:
            return False

        self.categories.remove(category)

        return True
    
    def add_payment_method(self, payment_method):

        payment_method = payment_method.strip()

        if not payment_method:
            return False

        if payment_method.lower() in [
            item.lower()
            for item in self.payment_methods
        ]:
            return False

        self.payment_methods.append(
            payment_method
        )

        return True
    
    def add_status(self, status):

        status = status.strip()

        if not status:
            return False

        if status.lower() in [
            item.lower()
            for item in self.status_list
        ]:
            return False

        self.status_list.append(
            status
        )

        return True
    
    def add_income_type(self, income_type):

        income_type = income_type.strip()

        if not income_type:
            return False

        if income_type.lower() in [
            item.lower()
            for item in self.income_types
        ]:
            return False

        self.income_types.append(
            income_type
        )

        return True