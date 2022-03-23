###########################################################
############ Trabalhando com Dicionarios #################

# Os dicionarios não possuem indice de memória e a identificação é feita por chave e valores
# Os dicionarios são mutáveis

dicionario = {'chave':'valor'}

frutas_iniciais= {"A": "Abacate", "M": "Melancia", "L": "Limão", "B": "Banana"}

print(frutas_iniciais)

print(frutas_iniciais['M'])

####### Iterar o dicionario com o for, pois ele também é um iterável

for d in frutas_iniciais:
    print(d + " "+frutas_iniciais[d])      ### aspas "" é para concatenar


for d in frutas_iniciais.items():         ### items saída em tupla
    print(d)

for d in frutas_iniciais.values():       ### valores
    print(d)

for d in frutas_iniciais.keys():        ### chaves
    print(d)


n_ruas= {
    (100,200): "Rua do Braz",
    (1,100): "Rua das Arvores",
    (50,230): "Rua dos Atletas"
}

print(n_ruas)

## 1) Forma de adicionar dados a um dicionario existente

n_ruas[(200,500)] = "Rua das Camélias"

print(n_ruas)

## Remover dados de um dicionário

del n_ruas[(1,100)]

print(n_ruas)

#### Atualizar ou adicionar um dicionario através de outro dicionario

nova_rua= {(200,501): "Rua José da Silva"}

n_ruas.update(nova_rua)

print(n_ruas)

#### Forma de inserir um valor de dicionairio com o comando update

n_ruas.update({(200,1000): "Rua Abilio Costa"})

print(n_ruas)

##### Extrair informações do dicionario com o comando pop

print(frutas_iniciais.pop("A"))

### Limpar os valores de um dicionario com o comando clear

frutas_iniciais.clear()
print(frutas_iniciais)

#### Copiar dados de um dicionario

novas_ruas= n_ruas.copy()
novas_ruas= n_ruas

print(novas_ruas)




