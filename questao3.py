def calcular_faturamento(faturamento):
    # Filtrar os dias sem faturamento 
    dias_com_faturamento = [f for f in faturamento if f > 0]

    # Cálculo de menor e maior faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    # Cálculo da média de faturamento (considerando apenas dias com faturamento)
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contagem de dias com faturamento acima da média
    dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_faturamento)

    # Exibição dos resultados
    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

    # Retorno dos resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Exemplo de vetor de faturamento diário, contendo valores que simulam dias sem faturamento
faturamento_diario = [
    1000, 1200, 0, 0, 800, 900, 0, 0, 1500, 1600, 0, 0, 1100, 1300, 0, 0, 
    2000, 1900, 0, 0, 900, 950, 0, 0, 1400, 1800, 0, 0, 0, 2500, 2100, 0
]

# Chamada da função para cálculo do faturamento
calcular_faturamento(faturamento_diario)

# Resultado para o vetor de exemplo acima:
# Menor faturamento: 800
# Maior faturamento: 2500
# Dias com faturamento acima da média: 7
