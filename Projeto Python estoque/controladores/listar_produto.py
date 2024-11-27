import funcionalidades
import funcionalidades.listar_produto_por_tipo

opcao_tipo = {
    "1": "cabelo",
    "2": "barba",
    "3": "pele",
    "4": "todos"
}

def executar():
    tipo = obter_tipo()
    funcionalidades.listar_produto_por_tipo.executar(tipo=tipo)

def obter_tipo():
    escolha = ""
    while escolha not in opcao_tipo:
        print("1 - Somente produto tipo cabelo")
        print("2 - Somente produto tipo barba")
        print("3 - Somente produto tipo pele")
        print("4 - Todos os produtos")

        escolha = input("Digite uma opção: ")
        if escolha in opcao_tipo:
            return opcao_tipo[escolha]
        print("\nOpção inválida")

