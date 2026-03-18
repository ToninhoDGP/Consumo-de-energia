nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {nome_aparelho} em Watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {nome_aparelho} fica ligado(a)? "))
consumo_mensal = (potencia * horas_dia * 30) / 1000
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh
print("-" * 30)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f}")
