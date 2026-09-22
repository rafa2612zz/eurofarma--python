#coletando renda e situação do correntista
renda = float(input("Digite sua renda mensal R$: "))
situação = input("possui restrição / nome negativo (s/n): ")

#validando renda e situação de restrição
emprestimo = (renda >= 3000) and situação == "n"

print("emprestimo aprovado: ", emprestimo)
