from servicos import obter_produtos


def executar(tipo):
    produtos = obter_produtos.executar()

    """se tipo diferente de "todos" eu vou filtrar com List Comprehensions  
    Comando .get serve para pegar alguma propriedade   
    """
    if tipo != "todos":
        produtos = [produto for produto in produtos if produto.get("tipo", "") == tipo]

    if len(produtos) == 0:
        print("Nenhum produto encontrado")
        return

    for produto in produtos:
        print("\n ------- // ------")
        for chave, valor in produto.items():
            
            """
            Esse é um if ternario, pra validar algo simples 
            
            """
            print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}") 
            



