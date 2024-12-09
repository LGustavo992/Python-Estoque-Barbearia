from funcionalidades import atualizar_produto

def executar():
    id_produto = input("Informe o ID da produto (somente números): ")

    # if id_produto.isnumeric() == False: <-(mesmo comando abqaixo de uma outra forma)
    if not id_produto.isnumeric():
        print("ID inválido")
        return
    atualizar_produto.executar(id_produto)