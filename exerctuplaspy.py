

tupla_numeros= (2,18,25,36)
tupla_numeros1 = 15,28,33,45
tupla_numeros2 = 88
tupla_numeros3 = 35,

print(type(tupla_numeros))
print(type(tupla_numeros1))
print(type(tupla_numeros2))
print(type(tupla_numeros3))
######################################################

t_frutas = "Pessego", "Morango", "Uva"

print(t_frutas[2])
###################################################

print(min(tupla_numeros))
################################################

t_concat= tupla_numeros+t_frutas

print(t_concat)
##########################################

frutas = input("Digite a fruta: ")

if frutas in t_frutas:
    print("A fruta existe")
else:
    print("A fruta não existe")            # Há diferença entre maiúsculas e minúsculas