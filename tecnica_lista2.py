#Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado
#Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora

def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
            #print(contagem[produto])
        else:
            contagem[produto] = 1
            #print(contagem[produto])
            #print(contagem)
    #print(contagem['Notebook'])
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        #print(produto)
        #print(count)
        #print(contagem.items())
        if count > max_count:
            max_produto = produto
            max_count = count

    #print(max_produto)
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.split(',')
    #print(produtos)
    produtos = [produto.strip() for produto in produtos]
    #print(produtos)
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
