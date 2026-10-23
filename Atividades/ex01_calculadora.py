import os
os.system("cls")

print("====CALCULADORA====")

while True:
    numero1 =  int(input("digite o 1° número: "))
    numero2 = int(input("digite o 2° número: "))       
    operador = input("digite qual o operador +, -, * ou /: ")
    os.system("cls")
    match operador:
        case "+":
            soma = numero1 + numero2
            print(soma)
            print(f"o operador escolhido foi: {operador} ")
            break
        case "-":
            subtracao = numero1 - numero2
            print(subtracao)
            print(f"o operador escolhido foi: {operador}")
            break
        case "*":
            multip = numero1 * numero2
            print(multip)
            print(f"o operador escolhido foi: {operador}")
            break
        case "/":
            if numero2 == 0:
                input(f"não é possivel dividir por 0.\ntente novamente")
                os.system("cls")
            else:
                div = numero1 / numero2
                print(div)
                print(f"o operador escolhido foi: {operador}")
                break
        case _:
            print("digite um operador válido.")