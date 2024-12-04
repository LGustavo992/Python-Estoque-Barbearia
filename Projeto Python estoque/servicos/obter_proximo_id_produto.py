from servicos import obter_produtos

def executar():
    produtos = obter_produtos.executar()

    if len(produtos) == 0:
        return '1'

    ultimo_produto = produtos[-1]
    proximo_id = int(ultimo_produto.get("id", 0)) + 1
    return str(proximo_id)