from servicos import obter_produtos, atualizar_produtos
from funcionalidades.utilidades import solicitar_tipo, solicitar_status

def executar(id_produto):
    produtos = obter_produtos.executar()
    posicao_encontrada = None
    """
    ENUMERATE converte uma tupla ou lista com enumerações antes dos valores
    """
    for posicao, produto in enumerate(produtos):
        if produto.get("id") == id_produto:
            posicao_encontrada = posicao
            break
    
    if posicao_encontrada is None:
        print(f"Nenhuma produto encontrada com esse ID {id_produto}")
        return
    
    print("\n-- produto encontrado --")
    print("(prescione 'enter' para manter o valor atual)")
    for chave, valor in produtos[posicao_encontrada].items():
        if chave == "id":
            continue

        novo_valor = ""
        mensagem = f"{chave} (atual: {valor})"

        if chave == "tipo":
            novo_valor = solicitar_tipo.executar(mensagem, aceita_vazio=True)
        elif chave == "status":
            novo_valor = solicitar_status.executar(mensagem, aceita_vazio=True)
        else:
            novo_valor = input(mensagem + ": ")
        
        produtos[posicao_encontrada][chave] = novo_valor if len(novo_valor) > 0 else valor

    foi_atualizado = atualizar_produtos.executar(produtos)
    if foi_atualizado:
        print("produto atualizada com sucesso")
        return
    
    print("Não foi possível atualizar a produto")

