idades = []

while True:
    idade = input("Digite a idade: ")
    
    if idade == "":
        
        break
    else:
        idade = int(idade)
        
        idades.append(idade)

print(idades)