# Criando a função nome completo

def nome_completo(nome,sobrenome):
    return f"{nome} {sobrenome}"

# Solicitando os dados do usuário

nome = input("digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")

nome_inteiro = nome_completo(nome_usuario,sobrenome_usuario) 
print(nome_inteiro)
