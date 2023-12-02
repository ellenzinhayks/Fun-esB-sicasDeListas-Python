#algumas funções básicas de lista

#tamanho de lista

#usaremos: tamanho=len(lista)

produtos = ['apple tv', 'mac', 'iphone x','Ipad','Apple Watch','Mac Book','Airpods',]

#quantos produtos temos a venda?

tamanho = len(produtos)
print('Temos {} produtos'.format(tamanho))

#maior e menor valor

#maior = max(lista)
#menor = min(lista)

vendas = [1000,1500,15000,270,900,100,1200]
#qual o item mais vendido?
#qual o item menos vendido?

mais_vendido = max (vendas)
menos_vendido = min (vendas)

print('O produto mais vendido teve {} unidades vendidas, e o menos vendido teve {} unidades.'.format(mais_vendido,menos_vendido))

i = vendas.index(mais_vendido)
produto_mais_vendido = produtos [i]
print(produto_mais_vendido)

#produto menos vendido

i = vendas.index(menos_vendido)
produto_menos_vendido = produtos [i]
print(produto_menos_vendido)