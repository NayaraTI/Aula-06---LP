############## Trabalhando com Tuplas #################
# As tuplas possuem a mesma funcionalidade que as listas e também pode ser usado as mesmas funções de uma lista, exceto se
#alterada, adicionada, ou excluida elementos da mesma
# Uma tupla não pode ser alterada, porém, pode ser refatorada (reescrita)

tupla_numeros = (1,2,56,45)
tupla_numeros1 = 24,67,12,89
tupla_numeros2 = 56
tupla_numeros3 = 45,             # tupla é definida por vírgula, não parênteses

print(type(tupla_numeros))
print(type(tupla_numeros1))
print(type(tupla_numeros2))    # 56 não é uma Tupla
print(type(tupla_numeros3))

# Uma Tupla é definida por vírgula, entre os seus valores.
# Uma Tupla só será utilizada entre parenteses quando ela estiver dentro de outra estrutura de dados
# Uma Tupla é a estrutura de dados mais rápida, devido a sua imutabilidade (consome menos memória)

# Ver o tamanho de dados de uma Tupla com a função len

print(len(tupla_numeros))

# Posição de memória

print(tupla_numeros[1])

# Executar cálculos em Tuplas

print(sum(tupla_numeros))  #soma
print(max(tupla_numeros))  #valor máximo

### Testando a imutabilidade da Tupla ###

print(tupla_numeros+tupla_numeros1)

tupla_numeros4 = tupla_numeros+tupla_numeros1

print(tupla_numeros4)

########## Refatorando(reescrevendo uma tupla para poder acrescentar valores) ########

tupla_numeros= tupla_numeros+tupla_numeros1

print(tupla_numeros)

###### Iterar uma tupla com for pois a tupla também é um iterável

for i in tupla_numeros:
    print(i)

####### Verificar se um dado está contido na tupla  #########

print(45 in tupla_numeros)

### Cópia de tupla ou qualquer estrutura de dados ###

copia_tupla =  tupla_numeros

print(copia_tupla)