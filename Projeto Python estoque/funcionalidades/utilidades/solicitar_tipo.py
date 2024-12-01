def executar(mensagem, aceita_vazio = "normal"):
    tipo = ""
    while tipo not in ["cabelo", "barba" , "pele"]:
        entrada_usuario = input(mensagem).lower()

        if aceita_vazio and entrada_usuario == "":
            return ""

        if entrada_usuario == "c":
            tipo = "cabelo"
        elif entrada_usuario == "b":
            tipo = "barba"
        elif entrada_usuario == "p":
            tipo = "pele"
        else:
            print("Tipo inválido")

    return tipo