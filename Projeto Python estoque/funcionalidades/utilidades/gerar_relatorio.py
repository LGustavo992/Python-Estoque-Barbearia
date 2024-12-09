from servicos import obter_produtos
def executar(mes):
    print(f"** Gerando relatório do mês {mes} **")

    produtos = obter_produtos.executar()
    produtos_relatorio = {
        'valor_total_credito': 0,
        'valor_total_debito': 0,
        'quantidade_pago': 0,
        'quantidade_cancelado': 0,
        'quantidade_pendente': 0,
        'valor_total': 0,
        'produtos_por_categoria': {

        },
    }