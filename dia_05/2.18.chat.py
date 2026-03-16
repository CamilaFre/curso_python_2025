#%%

frases = []

count = -1

pos = 0

while True:
    
    frase = input("Digite uma frase: ")

    if frase == "":
        break
    
    frases.append(frase)

print(frases)

tamanho = len(frases)

ultima_pos = tamanho - 1


for frase in frases:

    count += 1
    
    pos = 0
    
    soma = []   # reinicia a contagem da frase atual
    
    while pos <= ultima_pos:

        if frases[count] == frases[pos]:
            rept = 1
        else:
            rept = 0

        soma.append(rept)

        pos += 1

    print(frases[count], "-", sum(soma))
# %%
