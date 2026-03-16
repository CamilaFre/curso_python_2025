#%%

dados = {}

while True:

    frase = input("Digite uma frase: ")

    if frase == "":

        break


    if frase not in dados:

        dados[frase] = 1

    else:

        dados[frase] +=1

for i in dados:

    print(i, "->", dados[i])        
# %%
