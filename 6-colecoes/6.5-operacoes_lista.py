lista_inicial = ["joão","pamela","dominique"]
print("lista inicial:",lista_inicial)
print(60 * "-")

#======Acrescentando item na lista======
lista_inicial.append("Eduarda")
print("apos o append",lista_inicial)
print(60 * "-")

#======Acrescentando item na lista======
lista_inicial.insert(2,"matheus")
print("apos o append",lista_inicial)
print(60 * "-")

#=====Modificando um item da lista======
lista_inicial[3] = "Rafael"
print("Após modificacão: ",lista_inicial)
print(60 * "-")

#======Apagando item em indice especifico======
del lista_inicial[3]
print("Após modificacão: ",lista_inicial)
print(60 * "-")

#======Apagando item em indice especifico======
lista_inicial.remove("pamela")
print("Apos remove: ",lista_inicial)
print(60 * "-")

#======Apagando armazenando valor da lista======
remove = lista_inicial.pop(1)
print(f"Após pop, {remove}", lista_inicial)
print(60 * "-")

#======Limpando completamente a lista======
lista_inicial.clear
print("Apos remove: ",lista_inicial)
print(60 * "-")






















































