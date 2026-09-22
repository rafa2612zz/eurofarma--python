#solicitando nome e notas do aluno
nome = input("digite seu nome: ")
nota_1 = float(input("digite primeira nota: "))
nota_2 = float(input("digite segunda nota: "))
nota_3 = float(input("digite terceira nota: ")) 

#realizando o cálculo da média
media = (nota_1 + nota_2 + nota_3) / 3




if media < 4:
    situacao = "reprovado"
elif media < 6:
    situacao = ("recuperação")
else:
    situacao = ("aprovado")


print(f"A media do aluno(a) ,{nome} é {media:.1f} ele foi , {situacao}")