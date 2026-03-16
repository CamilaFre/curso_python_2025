#%%

frases = []

count = -1

soma = []

pos = 0

rept = 0

resultado = {}


while True:
    
    frase = input("Digite uma frase: ")

    if frase == "":
        break
    
    frases.append(frase)

print(frases)

tamanho = len(frases)

# print(tamanho)

ultima_pos = tamanho-1

# print(ultima_pos)


for frase in frases:

    count +=1
    
    pos = 0
    
    soma = []
    
    # print(count)



    while pos <= ultima_pos:

        # print(count)

        # print(pos)

        # print(pos)

        # print(frases[pos])

        # print(frases[count])
       
        if frases[count] == frases [pos]:

          

            rept = 1

           

        else:

            rept = 0
        
        pos+=1

        soma.append(rept)
    
    total = sum(soma)

    resultado = {frase : total}

    print (resultado)

   

    

  


  


    
    # while pos <= len(frases)-1:

    #     if frases[count] == frases[pos]:

    #         rept+=1

    #         pos+=1

    #         print(rept)


    #     else:
           
    #        break


        
       














# %%
