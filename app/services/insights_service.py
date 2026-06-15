class InsightsService:

    def analyze(self, transactions, total_income, total_expenses):

        insights = []

        if total_income == 0:
            return ["Sem renda cadastrada ainda."]

        spend_percentage = (total_expenses / total_income) * 100

        # 🚦 ALERTA DE GASTOS
        if spend_percentage <= 50:
            insights.append("🟢 Seus gastos estão saudáveis.")
        elif spend_percentage <= 80:
            insights.append("🟡 Atenção: seus gastos estão altos.")
        else:
            insights.append("🔴 Perigo: gastos muito acima do ideal.")

        # 💸 MAIOR CATEGORIA DE GASTO
        categories = {}

        for t in transactions:
            if t.transaction_type == "Despesa":
                categories[t.category] = categories.get(t.category, 0) + t.value

        if categories:
            top_category = max(categories, key=categories.get)
            insights.append(f"📊 Maior gasto: {top_category}")

        # 📈 PARTICIPAÇÃO DOS GASTOS
        insights.append(
            f"📉 Você gastou {spend_percentage:.1f}% da sua renda"
        )

        # 🔥 FREELANCE / SOBRAS
        remaining = total_income - total_expenses

        if remaining > 0:
            insights.append(
                f"💰 Você ainda tem R$ {remaining:.2f} disponível no mês"
            )
        else:
            insights.append(
                "⚠️ Você está no vermelho este mês"
            )

        return insights
    