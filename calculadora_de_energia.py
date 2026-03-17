nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {nome_aparelho} em Watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {nome_aparelho} fica ligado(a)? "))
consumo_mensal = (potencia * horas_dia * 30) / 1000
print("-" * 30)
print(f"Resultado para: {nome_aparelho}")
print(f"O consumo mensal estimado é de: {consumo_mensal:.2f} kWh")