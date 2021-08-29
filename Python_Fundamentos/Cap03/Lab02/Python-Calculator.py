"""Python Calculator"""

print("*"*20 + " Python Calculator " + "*"*20)

print("Selecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

option = input("Digite sua opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if option == "1":
    print("%s + %s = %s" %(num1, num2, num1 + num2))
elif option == "2":
    print("%s - %s = %s" %(num1, num2, num1 - num2))
elif option == "3":
    print("%s * %s = %s" %(num1, num2, num1 * num2))
elif option == "4":
    print("%s / %s = %s" %(num1, num2, num1 / num2))
else:
    print("Esta opção é inválida!")

