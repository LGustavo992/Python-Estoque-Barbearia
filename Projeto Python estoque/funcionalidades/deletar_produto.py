from servicos import obter_produtos, atualizar_produtos

def executar(id_produto):
    produtos = obter_produtos.executar()
    produto_encontrado = None

    for produto in produtos:
        if produto.get("id") == id_produto:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print(f"Nenhuma produto foi encontrada com o ID {id_produto}")
        return

    print("\n-- Produto Encontrado --")
    for chave, valor in produto_encontrado.items():
        print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}")

    escolha = input("\nDeseja excluir esse produto? (s/n): ")
    
    """
    LOWER serve para validar todas respostas em minusculo 
    """
    
    if escolha.lower() != "s":
        print("Operação cancelada")
        return
    """
    Para o usuário parece que foi exluido, mas a lógica é atualizar as alterações com uma nova lista por cima na verdade
    """
    produtos_filtrados = [produto for produto in produtos if produto.get("id") != id_produto]

    foi_deletado = atualizar_produtos.executar(produtos_filtrados)
    
    if foi_deletado:
        print("produto excluído com sucesso")
    else:
        print("produto não foi excluído")