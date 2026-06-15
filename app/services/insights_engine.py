class InsightsEngine:

    def analyze(self, transactions, total_income, total_expenses):

        insights = []

        if total_income == 0:
            return [
                {"type": "warning", "text": "Sem dados suficientes ainda"}
            ]

        percent = (total_expenses / total_income) * 100

        if percent <= 50:
            insights.append({
                "type": "success",
                "text": "Gastos controlados (até 50% da renda)"
            })
        elif percent <= 80:
            insights.append({
                "type": "warning",
                "text": "Atenção: gastos elevados (50% - 80%)"
            })
        else:
            insights.append({
                "type": "danger",
                "text": "Alerta: gastos acima de 80% da renda"
            })

        categories = {}

        for t in transactions:
            if t.transaction_type == "Despesa":
                categories[t.category] = categories.get(t.category, 0) + t.value

        if categories:
            top_category = max(categories, key=categories.get)

            insights.append({
                "type": "info",
                "text": f"Maior gasto em: {top_category}"
            })

        savings = total_income - total_expenses

        if savings > 0:
            insights.append({
                "type": "success",
                "text": f"Você economizou R$ {savings:.2f}"
            })
        else:
            insights.append({
                "type": "danger",
                "text": "Você está gastando mais do que ganha"
            })

        return insights
    