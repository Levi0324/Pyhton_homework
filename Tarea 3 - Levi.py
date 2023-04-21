# Tarea 3 Listas - Levi 

mi_lista = [] # No se imprime nada 

lista = [1, ['a', 'e', 'i', 'o', 'u'], 10, 'Hello World'] 

print (lista) # [1, ['a', 'e', 'i', 'o', 'u'], 10, 'Hello World']

lista.reverse()
print(lista)  # ['Hello World', 10, ['a', 'e', 'i', 'o', 'u'], 1]

lista=[10, 20, 35, 40, 45]
print(len(lista))    # imprime un 5
lista.append(100)
print(len(lista))    # imprime un 6
print(lista[0])      # imprime un 10
print(lista[5])      # imprime un 100