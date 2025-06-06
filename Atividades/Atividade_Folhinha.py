qntCamisa = int(input("Quantas camisas você quer comprar? "))
valorUni = 12.5

if qntCamisa<5:
    valor = qntCamisa*valorUni*0.97
elif qntCamisa>=5 and qntCamisa <=10:
    valor = qntCamisa*valorUni*0.95
elif qntCamisa>10:
    valor= qntCamisa*valorUni*0.93

print(f"{qntCamisa} camisas sairão por {valor} R$.")


