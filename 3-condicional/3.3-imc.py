# Solicitando os dados do paciente
nome = input("Digite o nome do paciente")
peso = float(input("digite o peso do paciente KG: "))
altura = float(input(" digite a altura do paciente m: "))

# Calclando o IMC do paciente
imc = peso / altura ** 2

# Definindo o quadro do paciente segundo o IMC
if imc < 18.5:
    situacao = "abaixo do peso"
elif imc <= 24.9:
    situacao = "peso normal"
elif imc <= 29.9:
    situacao = "sobrepeso"
elif imc <= 34.9:
    situacao = " obesidade grau 1"
elif imc <= 39.9:
    situacao = "obesidade grau 11"
else:
    situacao = "obesidade grau 111"
print(f"O IMC do paciente {nome} é {imc} e ele(a) esta {situacao}")