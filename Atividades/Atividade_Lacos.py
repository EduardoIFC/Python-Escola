import os, random, heapq
while True:
    atividade = input("Digite o numero da atividade que quer executar, 1 a 10.\n 0 Sai.  ")
    if atividade =="0":
        break
    if atividade == "1":
        #1-Faça um programa que leia infinitos números até que a soma ultrapasse 1000. Mostre quantos números foram digitados.
        soma = 0
        numeros = 0
        while soma < 1000:
            soma+=int(input("Digite um numero para adicionar a soma, quando ultrapassar de 1000, o programa sera terminado "))
            numeros+=1
        print(f"Foi digitado {numeros} numeros até a soma completar 1000.")
        os.system("clear")
    elif atividade == "2":
        #2-Desenvolva um sistema de login com limite de 3 tentativas.]
        for i in range(1,4,1):
            print(f"{i}ª tentativa. ")
            usuario = input("Qual o usuario? ")
            senha = input("Qual a senha? ")
            if senha == "admin" and usuario == "admin":
                print("Acesso liberado. ")
                break
            else:
                print("Senha e/ou usuario errados. ")
        else:
            print("tentativas esgotadas!")
    
    elif atividade == "3":
    #3-Calcule os 20 primeiros termos da sequência de Fibonacci.
        fibonnaci = [0,1]
        for i in range(2,21,1):
            fibonnaci.append(fibonnaci[i-2]+fibonnaci[i-1])
        print(fibonnaci)

    #4-Simule um caixa eletrônico que só encerra após sacar todos os valores (notas de 100, 50, 20, 10, 5, 2).
    elif atividade == "4":
        valor = int(input("Quantos tem no caixa?"))
        while valor > 0:
            print(f"Você tem {valor} R$ na conta.")
            retirado = int(input("Quantos quer sacar? (so pode notas existentes.)\n"))
            if valor - retirado >= 0:
                match retirado:
                    case 100|50|20|10|5|2: valor -= retirado
                    case _: print("Nota invalida.")
            else: 
                print("Valor invalido, saldo sera negativo.")
    #5-Monte um programa que peça números até que o usuário decida parar, e informe a média, maior e menor valor.
    elif atividade == "5":
        valores = []
        while True:
            try: valores.append(int(input("Qual numero quer adicionar? (digite qualquer coisa alem de numeros para parar de adicionar\n)")))
            except: break
        print(f"Média dos numeros adicionados: {sum(valores)/len(valores)}\nMaior numero: {max(valores)}\nMenor numero:{min(valores)}")
    #6-Leia nome e idade de várias pessoas até que a idade digitada seja negativa. Mostre quantas são maiores de idade.
    elif atividade == "6":
        idades = []
        nomes = []
        maiores = 0
        while min(idades)>=0:
            idades.append(int(input("Qual sua idade? ")))
            nomes.append(input("Qual o seu nome? "))
        for i,j in idades,enumerate:
            if i >= 18:
                maiores +=1
                print(f"O {nomes[j]} tem {idades}")
        print(f"Tem {maiores} maiores de idade.")
    #7-Faça um jogo de adivinhação com tentativas limitadas e dicas (maior/menor).
    elif atividade == "7":
        numero = random.randint(0,1000)
        while True:
            adivinhacao = int(input("Adivinhe qual numero é "))
            if adivinhacao > numero:
                print("Menor")
            elif adivinhacao < numero:
                print("Menor")
            else:
                break
        print("Acertou miseravi.")
    #8-Simule o cadastro de 5 produtos (nome e preço). Informe o mais caro e a média de preço.
    elif atividade == "8":
        produtos = []
        nomeProdut = []
        for i in range(5):
            produtos.append(int(input("Qual o valor do produto?")))
            nomeProdut.append(input("Qual o nome do produto."))
        print(f"Média do valor {sum(produtos)/5}.\nO valor  ")
    #9-Gere os 30 primeiros números primos.
    elif atividade == "9":
        n=3000
        primes_pool = [(4, 2)]
        heapq.heapify(primes_pool)
        primes = [2]
        for i in range(3, n+1):
            while primes_pool[0][0] < i:
                multiple, prime = heapq.heappop(primes_pool)
                heapq.heappush(primes_pool, (multiple + prime, prime))
            if primes_pool[0][0] == i:
                multiple, prime = heapq.heappop(primes_pool)
                heapq.heappush(primes_pool, (multiple + prime, prime))
            else:
                primes.append(i)
                heapq.heappush(primes_pool, (i*i, i))
        print("{}".format(', '.join([str(primes[i]) for i in range(30)])))


    #10-Crie uma calculadora com menu interativo (1 - somar, 2 - subtrair, etc.) e opção de sair.
    input("\n Question ended, press enter to choose other question. \n")
    os.system("clear")