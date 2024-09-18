def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:

    total_vendas = 0
    media_vendas = 0
    
    for venda in vendas:
        #print(venda)
        total_vendas += venda
        
    media_vendas = total_vendas / 12
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    #print(entrada)
    vendas = entrada.split(',')
    vendas = [int(i) for i in vendas]
    #print(vendas)
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
