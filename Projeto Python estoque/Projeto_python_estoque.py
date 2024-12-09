from datetime import datetime
from controladores import (
    criar_produto,
    excluir_produto, 
    listar_produto,
    atualizar_produto,
    gerar_relatorio
    )
from os import system

opcoes_menu = [
    "1 - Listar produto",
    "2 - Adicionar produto",
    "3 - Atualizar produto",
    "4 - Excluir produto",
    "5 - Gerar relatório de um mês",
    "6 - Encerrar",
]

def iniciar_menu():
    while True:
        print("\n- MENU PRINCIPAL -\n")

        for opcao in opcoes_menu:
            print(opcao)
        
        opcao_escolhida = input("\nDigite uma opção: ")
        
        match opcao_escolhida:
            case '1':
                print("\n ** LISTAR PRODUTO ** \n")
                listar_produto.executar()
                #...
            case '2':
                print("\n ** CRIAR UM NOVO PRODUTO ** \n")
                criar_produto.executar()
                #...
            case '3':
                print("\n ** ATUALIZAR UM PRODUTO ** \n")
                #...
            case '4':
                print("\n ** EXCLUIR UM PRODUTO ** \n")
                excluir_produto.executar()
                #...
            case '5':
                print("\n ** GERAÇÃO DE RELATÓRIO  ** \n")
                gerar_relatorio.executar()
            case '6':
                print("\n ** PROGRAMA ENCERRADO  ** \n")
                break
                #...
            case _:
                print("\n OPÇÃO INVÁLIDA \n")

if __name__ == "__main__":
    system('clear')
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()
    


 