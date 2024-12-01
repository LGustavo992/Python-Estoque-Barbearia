from funcionalidades.utilidades import solicitar_tipo, validar_data, solicitar_status
from servicos import obter_proximo_id_produto, salvar_produto

def executar():
    print("**Informe os dados abaixo **")

    descricao = input("Qual é a descrição? ")
    valor = input("Qual é o valor? ")
    tipo = solicitar_tipo.executar("Qual é o tipo? (c = cabelo, b = barba, p = pele) ")
    categoria = input("Qual é a categoria? ")
    data_compra = validar_data.executar(input("Qual é a data de compra? (DD/MM/YYYY) "))
    status = solicitar_status.executar()
    data_venda = input("Qual é a data de venda? (DD/MM/YYYY) ")

    if status == "pago":
        data_venda = validar_data.executar(data_venda)

    novo_produto = {
        "id": obter_proximo_id_produto.executar(),
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
        "data_compra": data_compra,
        "data_venda": data_venda,
        "status": status,
    }

    foi_persistido = salvar_produto.executar(novo_produto)

    if foi_persistido:
        print("Novo produto salvo com sucesso")
    else:
        print("Não foi possível salvar o produto")


