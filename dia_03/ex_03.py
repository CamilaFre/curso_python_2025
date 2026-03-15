
soma_saldo = 0

while True:
    
    saldo = input ("Digite o saldo em conta ")

    if saldo =="":
        break

    
    soma_saldo += float(saldo)

print (soma_saldo)