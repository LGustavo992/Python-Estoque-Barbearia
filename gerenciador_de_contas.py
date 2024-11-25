import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Criação da tabela no banco de dados
def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        fornecedor TEXT NOT NULL
    )
    """)
    conn.commit()

# 1. Criar - Registrar novo produto
def criar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    preco_unitario = float(input("Preço unitário: "))
    fornecedor = input("Fornecedor: ")

    cursor.execute("""
    INSERT INTO produtos (nome, quantidade, preco_unitario, fornecedor)
    VALUES (?, ?, ?, ?)
    """, (nome, quantidade, preco_unitario, fornecedor))
    conn.commit()
    print(f"Produto '{nome}' registrado com sucesso!")

# 2. Listar - Exibir todos os produtos
def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\nProdutos cadastrados:")
        for p in produtos:
            print(f"ID: {p[0]}, Nome: {p[1]}, Quantidade: {p[2]}, Preço: R$ {p[3]:.2f}, Fornecedor: {p[4]}")
    else:
        print("Nenhum produto cadastrado.")

# 3. Atualizar - Alterar dados de um produto
def atualizar_produto():
    id_produto = int(input("Informe o ID do produto que deseja atualizar: "))
    campo = input("Informe o campo que deseja atualizar (nome, quantidade, preco_unitario, fornecedor): ")
    novo_valor = input(f"Novo valor para {campo}: ")

    if campo in ["quantidade", "preco_unitario"]:
        novo_valor = float(novo_valor)

    cursor.execute(f"UPDATE produtos SET {campo} = ? WHERE id = ?", (novo_valor, id_produto))
    conn.commit()
    print("Produto atualizado com sucesso!")

# Atualizar estoque (entrada/saída)
def atualizar_estoque():
    id_produto = int(input("Informe o ID do produto: "))
    movimento = input("Movimento (entrada/saída): ").lower()
    quantidade = int(input("Quantidade: "))

    cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if not produto:
        print("Produto não encontrado.")
        return

    nome, estoque_atual = produto
    if movimento == "entrada":
        novo_estoque = estoque_atual + quantidade
    elif movimento == "saída":
        if quantidade > estoque_atual:
            print("Quantidade insuficiente no estoque.")
            return
        novo_estoque = estoque_atual - quantidade
    else:
        print("Movimento inválido.")
        return

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (novo_estoque, id_produto))
    conn.commit()
    print(f"Estoque do produto '{nome}' atualizado com sucesso!")

# 4. Deletar - Remover um produto
def deletar_produto():
    id_produto = int(input("Informe o ID do produto que deseja deletar: "))
    confirmacao = input(f"Tem certeza que deseja deletar o produto {id_produto}? (s/n): ")

    if confirmacao.lower() == "s":
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        print("Produto deletado com sucesso!")
    else:
        print("Operação cancelada.")

# Relatório de produtos em baixa quantidade
def relatorio_baixa_quantidade():
    limite = int(input("Informe o limite de quantidade para considerar baixa: "))
    cursor.execute("SELECT * FROM produtos WHERE quantidade <= ?", (limite,))
    produtos = cursor.fetchall()

    if produtos:
        print("\nProdutos em baixa quantidade:")
        for p in produtos:
            print(f"ID: {p[0]}, Nome: {p[1]}, Quantidade: {p[2]}, Fornecedor: {p[4]}")
    else:
        print("Nenhum produto com quantidade baixa encontrada.")

# Relatório financeiro do estoque
def relatorio_financeiro():
    cursor.execute("SELECT SUM(quantidade * preco_unitario) FROM produtos")
    total = cursor.fetchone()[0]

    if total:
        print(f"\nValor total do estoque: R$ {total:.2f}")
    else:
        print("O estoque está vazio.")

# Menu principal
def menu():
    criar_tabela()
    while True:
        print("\nGerenciador de Inventário")
        print("1. Criar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Atualizar estoque (entrada/saída)")
        print("5. Deletar produto")
        print("6. Relatório de produtos em baixa quantidade")
        print("7. Relatório financeiro do estoque")
        print("8. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            criar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            atualizar_estoque()
        elif opcao == 5:
            deletar_produto()
        elif opcao == 6:
            relatorio_baixa_quantidade()
        elif opcao == 7:
            relatorio_financeiro()
        elif opcao == 8:
            print("Saindo...")
            break
        else:
            print
