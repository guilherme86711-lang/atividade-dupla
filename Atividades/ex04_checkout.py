import os
os.system('cls')

print('''
METODO          DESCONTO / PARCELAS
1. À vista      10% Desconto
2. A prazo      6 parcelas max
''')

while True:
    op = int(input('Digite a opção escolhida: '))
    valor = float(input('Digite o Valor: '))
    
    match op:
        case 1:
            pagamento = 'À vista'
            desconto = valor * 0.10
            total = valor - desconto
            
            print('\n--- RESULTADO ---')
            print(f'Valor: {valor} ')
            print(f'Forma de pagamento: {pagamento} ')
            print(f'Desconto: {desconto}')
            print(f'Total: {total}')
            break
        case 2:
            prazo = int(input('Digite a quantidade de parcelas:'))
            pagamento = 'Parcelado'
            parcelas = valor // prazo
            total = valor
            
            print('\n--- RESULTADO ---')
            print(f'Valor: {valor} ')
            print(f'Forma de pagamento: {pagamento} ')
            print(f'parcelas: {prazo}')
            print(f'Valor das parcelas: {parcelas}')
            print(f'Total: {total}')
            break
        case _:
            print('\nOpção invalida digite: (1/2) pra continuar: ')
            continue