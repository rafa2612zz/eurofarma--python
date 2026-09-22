# criando função maior_numero
def maior_numero(x,y):
    if x > y:
        return x 
    else:
        return y 

#solicitando os dois numeros ao usuário
numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite outro numero: ")) 

#chamando a função que verifica o maior número
resultado = maior_numero(numero_1,numero_2)

#apresentando o maior numero ao usuário
print(f"o maior numero digitado foi {resultado}")


