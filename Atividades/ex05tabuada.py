import os
import time
os.system("cls")

numero = int(input(f"digite o seu numero: "))


for i in range(1, 11):
    print(f"digite o {i}: {numero*i}")
    time.sleep(1)