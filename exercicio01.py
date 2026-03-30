# exercios 

#a
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = num1 * num2

print("Resultado da multiplicação:", resultado)



#b
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
n4 = float(input("Digite o 4º número: "))
n5 = float(input("Digite o 5º número: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

print("Média aritmética:", media)



#c
valor = float(input("Digite o valor do produto: "))

imposto = valor * 0.08
preco_final = valor + imposto

print("Preço final com imposto:", preco_final)






#D
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = num1 - num2

print("Resultado da subtração:", resultado)


#e
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)



#f
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperatura em Fahrenheit:", fahrenheit)


#g
horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))

salario = horas * valor_hora

print("Salário total:", salario)
