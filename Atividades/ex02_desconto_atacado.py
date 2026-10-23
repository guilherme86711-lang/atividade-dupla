import os
os.system('cls')

print('''
ITENS           PREÇO
1. MACARRÃO     R$ 25.00
2. ARROZ        R$ 20.00
3. FEIJÃO       R$ 15.00
4. MONSTER      R$ 10.00
5. FARROFA      R$ 5.00
''')

while True:
    op = int(input('Digite o item escolhido: '))
    match op:
        case 1:
            nome = 'macarrão'
            preco = 25.00
        case 2:
            nome = 'arroz'
            preco = 20.00
        case 3:
            nome = 'feijão'
            preco = 15.00
        case 4:
            nome = 'monster'
            preco = 10.00
        case 5:
            nome = 'farrofa'
            preco = 5.00
        case _:
            print('Item não registrado')
            continue
    
    qtd = int(input('Digite a quantidade que quer: '))
    total = qtd * preco
    
    if qtd >= 10:
        dsct = total * 0.05
    elif qtd >= 6:
        dsct = total * 0.03
    elif qtd >= 5:
        dsct = total * 0.02
    else:
        dsct = 0
        
    total_pagar = total - dsct
    break
    
print('--- VALOR --- ')
print(f'Item: {nome}')
print(f'Preço: {preco:.2f}')
print(f'Total: {total:.2f}')
print(f'Desconto: {dsct:.2f}')
print(f'Total a pagar: {total_pagar:.2f}')