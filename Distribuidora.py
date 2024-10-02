import json

try:
    with open('distribuidora.json', 'r') as file:
        dados = json.load(file)
except FileNotFoundError:
    print("Arquivo 'distribuidora.json' não encontrado.")
    exit()

faturamento = dados['faturamento_diario']

faturamento.sort(key= lambda x: x['valor'])
print(f'Menor valor de faturamento ocorrido em um dia do mês , foi Dia {faturamento[0]['dia']} -> valor: {faturamento[0]['valor']}')
print(f'Maior valor de faturamento ocorrido em um dia do mês , foi Dia {faturamento[-1]['dia']} -> valor: {faturamento[-1]['valor']}')

valores_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
media = sum(valores_validos) / len(valores_validos)
dias_acima_da_media = [dia for dia in faturamento if dia['valor'] > media]
dias_acima_da_media.sort(key= lambda x: x['dia'])

print(f"Média do faturamento: {media:.2f}")#round(media, 2)
print("Dias acima da media")
for dia in dias_acima_da_media:
    print(f'Dia: {dia['dia']} -> Valor: {dia['valor']}')



