funcionarios = [{
    "nome": "Pedro",
    "nivel": "Sênior",
    "anoAdmissao": 2018,
    "salario": 15000
},{
    "nome": "Roberta",
    "nivel": "Sênior",
    "anoAdmissao": 2023,
    "salario": 12500
},{
    "nome": "Carlos",
    "nivel": "Pleno",
    "anoAdmissao": 2022,
    "salario": 8250
},{
    "nome": "Júlia",
    "nivel": "Júnior",
    "anoAdmissao": 2024,
    "salario": 6010
}]

#exemplo para calcular %
# valor = 0.05 * 100

def novo_salario(funcionario):
    # Calcula o tempo de serviço (ano atual - ano de admissão)
    ano_atual = 2024
    tempo_servico = ano_atual - funcionario["anoAdmissao"]

    # Aumento de 5%
    aumento_salario = funcionario["salario"] * 0.05

    # Adiciona 2% se o funcionário for sênior
    if funcionario["nivel"] == "Sênior":
        aumento_salario += funcionario["salario"] * 0.02

    # Adiciona 1% se o funcionário tiver mais de 2 anos de serviço
    if tempo_servico > 2:
        aumento_salario += funcionario["salario"] * 0.01

    # Atualiza o salário com o aumento total
    funcionario["salario"] += aumento_salario

# Atualizando o salário de cada funcionário na lista
for funcionario in funcionarios:
    novo_salario(funcionario)

# Apresentando os resultados
for funcionario in funcionarios:
    print(f"Funcionário: {funcionario['nome']}")
    print(f"Novo salário: R${funcionario['salario']:.2f}\n")