def executar():
    produtos = []

    try: 
        with open("dados/produtos.csv", "r", encoding="utf8") as arquivo:
            linha_atual = 0
            for linha in arquivo:
                if linha_atual == 0:
                    linha_atual += 1
                else:
                    valores = linha.splt(",")
                    produto = {
                            "id" : valores[0].strip(),
                            "descricao" : valores[1].strip(),
                            "valor" : valores[2].strip(),
                            "tipo" : valores[3].strip(),
                            "data de compra" : valores[4].strip(),
                            "data de venda" : valores[5].strip(),
                            "categoria" : valores[6].strip(),
                            "status" : valores[7].strip(),
                            
                    }
                    produtos.append(produto)
    except FileNotFoundError:
            print("Arquivo dados/produtos.csv não encontrado")
    except Exception as erro:
            print("Ocorreu um erro desconhecido", erro)

    return produtos