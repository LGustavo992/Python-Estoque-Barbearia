from funcionalidades import deletar_produto 

def executar():
    id_produto = input("Informe o ID da produto (somente números): ")
    """
    ISNUMERIC é uma função booleana, na qual ela retorna TRUE caso seja um número, ou FALSE caso seja uma letra (caso haja um numerp -3 ou 3.5 por exemplo ela retona FALSE pois "-" e "." são string)
    """
    if not(id_produto.isnumeric()):
        print("ID inválido")
        return
    
    deletar_produto.executar(id_produto=id_produto)

