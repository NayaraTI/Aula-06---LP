
dicionario= {'chave': 'valor'}

carros= {"G": "Gol", "M": "Mercedes", "A": "Audi"}

print(carros)

for d in carros.items():
    print(d)

for d in carros:
    print(d+ " "+carros[d])

for d in carros.values():
    print(d)

for d in carros.keys():
    print(d)


n_ruas= {
    (50,100): "Rua das flores",
    (100,200): "Rua das hortas",
    (200,300): "Rua das rosas"

}
print(n_ruas)

n_ruas[(300,400)] = "Rua dos arbustos"
print(n_ruas)

del n_ruas[(200,300)]
print(n_ruas)

nova_rua= {(400,500): "Rua das matas"}
n_ruas.update(nova_rua)
print(n_ruas)

print(carros.pop("M"))

novas_ruas= n_ruas.copy()
novas_ruas= n_ruas
print(novas_ruas)

novos_carros= carros.copy()
novos_carros= carros
print(novos_carros)