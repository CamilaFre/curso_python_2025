frutas ={
"Maçã": "R$1,50",
"Banana": "R$2,75",
"Uva": "R$1,90",
"Pera": "R$1,25",
"Laranja": "R$0,65",
"Limão": "R$1,25",
"Goiaba": "R$2,15",
"Abacaxi": "R$3,20",
"Jaca": "R$5,80",
}

chave = input("Digite o nome da fruta: ")

if chave in frutas:
    valor = frutas[chave]
    print(valor)
else:
    print("Digite um valor válido")