def  soma (x,y):
    soma_numeros = x + y
    return soma_numeros

def subtraçao (x,y):
    sub = x - y
    return sub

def divisao (x,y):
    div = x / y
    return div 

def multiplicaçao (x,y):
    multi = x * y 
    return multi


numero_1 = float(input("digite um numero: ")) 
numero_2 = float(input("digite outro numero: "))


resultado1 = soma (numero_1, numero_2)
resultado2 = subtraçao (numero_1, numero_2)
resultado3 = divisao (numero_1, numero_2 )
resultado4 = multiplicaçao (numero_1, numero_2) 

aleatorio = input("escolha uma alternativa (+, -, /, *): ")

if aleatorio == "+":
    print(resultado1)
elif aleatorio == "-":
    print(resultado2)
elif aleatorio == "/":
    print(resultado3)
elif aleatorio == "*":
    print(resultado4)
