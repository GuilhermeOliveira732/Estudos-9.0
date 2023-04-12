# Usando a função zip em listas para retornar tuplas
lista1 = [1,2,3,4]
lista2 = [1,2,3]

lista3 = list(zip(lista1, lista2))
print(lista3)

lista4 = list(zip([1,2,3,4], [1,2,3]))
print(lista4)

lista5 = list(zip([1,2,3,4], [5,6,7,8,9,10]))
print(lista5)

# Usando a função zip em dicionários

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
lista6 = list(zip(d1, d2))
print(lista6)
lista7 = list(zip(d1.values(), d2.values()))
print(lista7)

# Retorno é sempre em tuplas ('listas imutáveis')

# Exemplos de uso da função Enumerate

seq = ['a','b','c']
lista8 = list(enumerate(seq))
# Tanto zip quanto enumerate devem ser convertidos em list, do contrário ficarão como iteração
print(lista8)

# Perceba que o resultado [(0, 'a'), (1, 'b'), (2, 'c')] é o índice (0,1,2) com seu
# respectivo elemento ('a','b','c')
# Podemos utilizar o índice como ponto para finalização de uma execução de uma ação,
# por exemplo, executar a ação apenas até o índice 3, a seguir

seq1 = ['a','b','c','d','e','f','g']
lista9 = list(enumerate(seq1))
print(lista9)

for indice, valor in enumerate(seq1):
    if indice >= 3:
        break
    else:
        print(valor)



