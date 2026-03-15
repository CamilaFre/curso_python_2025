#%%

texto = """

Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás

"""

agua = int(input(texto))

qtde = int(input("Qual a quantidade desejada?"))

if agua == 1:
    preco = qtde*1.5
    print("O preço é R$", preco)
 
elif agua == 2:
     preco = qtde*2.5
     print("O preço é R$", preco)

else:
     print("Entre com a qtde correta")

# %%
