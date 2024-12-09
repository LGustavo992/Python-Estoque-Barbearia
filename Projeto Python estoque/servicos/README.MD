# Gerenciador de estoque de barbearia
Sistema para controle de produtos e serviçoes de uma barbearia. Registros de despesas e receitas, consultas avançadas, atualização de dados e geração de relatórios.

# Funcionalidades
- Criar (Create):
    - Registro de produtos.
    - Informações a serem salvas:
        - Tipo: Cabelo, Barba, Pele, quimica.
        - Descrição: Ex.: "Corte infantil", "depilação nariz e orelha".
        - Valor: Quantia em moeda local.
        - Data de compra.
        - Data de venda.
        - Categoria: Ex.: "Pomada", "Balm", "Esfoliante".
        - Status: Pago, Recebido ou Pendente.
- Ler (Read):
    - Visualização de uma lista dos produtos registrados, com filtros por:
        - Tipo (Cabelo, barba, pele, quimica)
        - Status (pago, pendente, cancelado)
        - Todos
- Atualizar (Update):
    - Alteração de qualquer informação previamente registrada.
- Excluir (Delete):
    - Remoção de produtos registrados.
    - Opção de confirmação para evitar exclusões acidentais.
- Gerar relatório (PDF) do mês
    - Gerar dados do mês atual com a soma das despesas e receitas
    - Listar as produtos utilizadas nos cálculos agrupados por data