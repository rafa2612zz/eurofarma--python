nome = input("Digite o nome do paciente: ")
ano = int(input("digite o seu ano de nascimento : "))

idade = 2026 - ano

if idade < 0:
    situacao = "RN"
elif idade < 3:
    situacao = "bebe"
elif idade < 10:
    situacao = "crianca"
elif idade < 12:
    situacao = "adolecenes"
elif idade < 25:
    situacao = "jovem"
else: idade < 30


print(f"voce {nome} é um(A) {situacao}")