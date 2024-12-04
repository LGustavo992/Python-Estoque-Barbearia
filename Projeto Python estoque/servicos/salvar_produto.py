def executar(nova_conta):
    try:
        with open("dados/produtos.csv", "a", encoding="utf8") as arquivo:
            """
            funcionalidade JOIN foi passado uma lista de texto e quero transformar numa STRING só , e a "," é usada como um separador das strings
            """
            
            linha = "\n" + ",".join([
                nova_conta["id"],
                nova_conta["descricao"],
                nova_conta["valor"],
                nova_conta["tipo"],
                nova_conta["data_compra"],
                nova_conta["data_venda"],
                nova_conta["categoria"],
                nova_conta["status"],
            ])
            arquivo.write(linha)
        return True
    except Exception as erro:
        print("\n Erro: ", erro)
        return False