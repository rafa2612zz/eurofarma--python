# solicitando o nome e a idade do usuario
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
possui_carteira = input("possui carteira de motorita s/n: ")

# criando a condição caso for >= a 18anos
if idade >= 18:
    if possui_carteira == "s" :
       print("pode dirigir")
    else:
        print("nao pode dirigir")

else:
    print("menor de idade")                                                             