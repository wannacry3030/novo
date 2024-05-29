import  tkinter
from tkinter import messagebox

num1 = float(input("Digita o primeiro numero: "))
num2 = float(input("Digita o segundo numero: "))
operacao = (input("Escolha a operacao (+, -, *, /)"))

#realizar as operacoes
if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado da subtracao é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado da multiplicacao é: {resultado}")
elif operacao == '/':
  if num2 != 0:
      resultado = num1 / num2
      print(f"O resultado da divisao é: {resultado}")
  else:
      print("Erro: Divisão por zero não é permitida")
else:
    print("operacao invalida. Por favor, escolha etre + - * /")