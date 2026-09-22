# Solicitando idade e se é estudante 
idade = int(input("Digite sua idade"))
estudante = input(" Voce é estudante s/n: ")

# validando o resultado ao usuário8
meia = (idade >= 60) or estudante == "s"

# Apresentando o resultado ao usuário
print ("Tem direito a meia-entrada ", meia)