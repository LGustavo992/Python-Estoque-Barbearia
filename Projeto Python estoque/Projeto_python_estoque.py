from datetime import datetime
from controladores import criar_produto, excluir_produto, listar_produto

opcoes_menu = [
    "1 - Listar produto",
    "2 - Adicionar produto",
    "3 - Atualizar produto",
    "4 - Excluir produto",
    "5 - Encerrar",
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
                print("\n ** PROGRAMA ENCERRADO  ** \n")
                break
                #...
            case _:
                print("\n OPÇÃO INVÁLIDA \n")

if __name__ == "__main__":
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()











# Conexão com o banco de dados
conn = sqlite3.connect("barbearia_estoque.db")
cursor = conn.cursor()

# Criação das tabelas
def criar_tabelas():
    cursor.execute("""
    CRIAR TABELA SE NÃO EXISTIR produto (
        id INTEIRO ,
        nome TEXTO Não NULO,
        preço REAL NÃO NULO,
        quantidade INTEGEIRO NAO NULO
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS despesas_receitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL, -- "despesa" ou "receita"
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL
    )
    """)
    conn.commit()

# Adicionar produto
def adicionar_produto(nome, preco, quantidade):
    cursor.execute("INSERT INTO produto (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conn.commit()
    print(f"Produto '{nome}' adicionado com sucesso.")

# Atualizar produto
def atualizar_produto(id_produto, nome=None, preco=None, quantidade=None):
    if nome:
        cursor.execute("UPDATE produto SET nome = ? WHERE id = ?", (nome, id_produto))
    if preco is not None:
        cursor.execute("UPDATE produto SET preco = ? WHERE id = ?", (preco, id_produto))
    if quantidade is not None:
        cursor.execute("UPDATE produto SET quantidade = ? WHERE id = ?", (quantidade, id_produto))
    conn.commit()
    print(f"Produto ID {id_produto} atualizado com sucesso.")

# Consultar produto
def consultar_produto():
    cursor.execute("SELECT * FROM produto")
    produto = cursor.fetchall()
    for produto in produto:
        print(produto)

# Registrar despesa ou receita
def registrar_movimentacao(tipo, descricao, valor):
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO despesas_receitas (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)",
                   (tipo, descricao, valor, data))
    conn.commit()
    print(f"{tipo.capitalize()} registrada com sucesso: {descricao} - R$ {valor:.2f}")

# Gerar relatório de despesas e receitas
def gerar_relatorio():
    cursor.execute("SELECT * FROM despesas_receitas")
    movimentacoes = cursor.fetchall()
    total_receitas = 0
    total_despesas = 0
    print("\n=== Relatório de Movimentações ===")
    for mov in movimentacoes:
        tipo, descricao, valor, data = mov[1], mov[2], mov[3], mov[4]
        print(f"{tipo.capitalize()}: {descricao} - R$ {valor:.2f} em {data}")
        if tipo == "receita":
            total_receitas += valor
        elif tipo == "despesa":
            total_despesas += valor
    print(f"\nTotal de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo Final: R$ {total_receitas - total_despesas:.2f}")

# Inicialização do sistema
if __name__ == "__main__":
    criar_tabelas()
    while True:
        print("\n=== Gerenciador de Estoque ===")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Consultar produto")
        print("4. Registrar Receita/Despesa")
        print("5. Gerar Relatório")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, preco, quantidade)
        elif opcao == "2":
            id_produto = int(input("ID do produto a atualizar: "))
            nome = input("Novo nome (ou deixe em branco): ")
            preco = input("Novo preço (ou deixe em branco): ")
            quantidade = input("Nova quantidade (ou deixe em branco): ")
            atualizar_produto(id_produto, nome or None, float(preco) if preco else None, int(quantidade) if quantidade else None)
        elif opcao == "3":
            consultar_produto()
        elif opcao == "4":
            tipo = input("Tipo (receita/despesa): ").lower()
            descricao = input("Descrição: ")
            valor = float(input("Valor: "))
            registrar_movimentacao(tipo, descricao, valor)
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
