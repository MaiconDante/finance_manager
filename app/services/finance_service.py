from app.database import repository
from app.services.insights_engine import InsightsEngine

class FinanceService:

    def __init__(self):

        repository.create_table()

        self.transactions = repository.get_all_transactions()

        self.insights_engine = InsightsEngine()

        self.load_settings()

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

        repository.insert_setting(
            "category",
            category
        )

        self.categories.append(category)

        return True
    
    def remove_category(self, category):

        if category not in self.categories:
            return False

        repository.delete_setting(
            category,
            "category"
        )

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

        repository.insert_setting(
            "payment",
            payment_method
        )

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

        repository.insert_setting(
            "status",
            status
        )

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

        repository.insert_setting(
            "income_type",
            income_type
        )

        self.income_types.append(
            income_type
        )

        return True
    
    def load_settings(self):


        self.categories = repository.get_settings(
            "category"
        )


        self.payment_methods = repository.get_settings(
            "payment"
        )


        self.status_list = repository.get_settings(
            "status"
        )


        self.income_types = repository.get_settings(
            "income_type"
        )


        if not self.categories:


            default_categories = [

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


            for item in default_categories:

                self.add_category(item)



        if not self.payment_methods:


            default_payments = [

                "PIX",
                "Cartão de Crédito",
                "Dinheiro",
                "Boleto",
                "Débito",
                "Outros"

            ]


            for item in default_payments:

                self.add_payment_method(item)



        if not self.status_list:


            for item in [

                "Pendente",
                "Pago",
                "Cancelado"

            ]:

                self.add_status(item)



        if not self.income_types:


            for item in [

                "Salário",
                "Freelance",
                "Investimento",
                "Décimo Terceiro",
                "PIS/PASEP",
                "Outros"

            ]:

                self.add_income_type(item)