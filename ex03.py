import os
os.system('cls')

renda_mensal = float(input("Digite a renda mensal do cliente (R$): "))
valor_emprestimo = float(
    input("Digite o valor total do empréstimo solicitado (R$): ")
)
num_prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = valor_emprestimo / num_prestacoes

emprestimo_valido = valor_emprestimo <= (renda_mensal * 10)
prestacao_valida = valor_prestacao <= (renda_mensal * 0.30)

os.system('cls')

print("\n--- Resultado da Pré-Análise ---")
print(f"Valor da prestação: R$ {valor_prestacao:.2f}")

if emprestimo_valido and prestacao_valida:
    print("Status: Crédito APROVADO!")
else:
    print("Status: Crédito NEGADO!")
    if not emprestimo_valido:
        print(
            "- Motivo: O valor do empréstimo ultrapassa 10x a renda mensal."
        )
    if not prestacao_valida:
        print(
            "- Motivo: O valor da prestação ultrapassa 30% da renda mensal."
        )