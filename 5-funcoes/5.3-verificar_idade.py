# Criando a função verificar_idade

def verificar_idade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade" 

# Solicitando a idade do usuário

idade_usuário = input("Digite sua idade : ")

resultado = verificar_idade(idade_usuário)

print(resultado)



print(f"bem-vindo, {nome_i

