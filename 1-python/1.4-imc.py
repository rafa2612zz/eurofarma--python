# solicitando peso altura ao usuario 
peso = float(input("Digite seu peso (KG): "))
altura = float(input("digite sua altura (M): "))

# Realizando o calculo do imc
imc = peso / altura**2

#apresentando o resultado do imc ao usuario
print("o seu IMC é ", imc)