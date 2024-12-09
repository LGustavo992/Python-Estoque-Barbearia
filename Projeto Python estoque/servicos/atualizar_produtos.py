def executar(novos_produtos):
    linhas = []
    for produto in novos_produtos:
        linha = "\n" + ",".join(
            [
                produto["id"],
                produto["descricao"],
                produto["valor"],
                produto["tipo"],
                produto["data_compra"],
                produto["data_venda"],
                produto["categoria"],
                produto["status"],
            ]
        )
        """
        APPEND é uma função de lista, que eu vou adicionar no final da lista um novo valor, no qual é LINHA
        """
        linhas.append(linha)
    
    primeira_linha = "id, descricao, valor, tipo, data vencimento, data pagamento, categoria, status"
   
    """
    INSERT serve para inserir um valor, mas eu decido qual lugar eu quero inserir
    """
    linhas.insert(0, primeira_linha)
    """
    Usado para abrir arquivo CSV
    """
    try:
        with open("dados/produtos.csv", "w", encoding="utf8") as arquivo:
            """
            WRITELINES passa uma lista de string e ele vai substituir todo meu arquivo
            """
            arquivo.writelines(linhas)
        return True
    except Exception as erro:
        print("Ocorreu um erro desconhecido ao tentar atualizar os dados", erro)
        return False