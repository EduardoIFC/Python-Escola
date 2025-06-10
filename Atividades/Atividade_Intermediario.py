import os
while True:
    input()
    os.system("clear")
    atividade = int(input("Qual atividade quer executar \n(1 a 10 = intermediario)\n(11 a 20 = avançado)\n(0 para sair)\n"))
    if atividade == 0:
        print("Saindo...")
        break
    elif atividade == 1:
        nota = float(input("Insira a nota. (1 a 10) :")) 
        if nota < 6:
            print("F")
        elif nota >= 9:
            print("A")
        elif nota >= 8:
            print("B")
        elif nota >= 7:
            print("C")
        elif nota >= 6:
            print("D")
    elif atividade == 2:
        peso = float(input("Qual o seu peso? "))
        altura = float(input("Qual a sua altura? "))
        imc = peso / (altura**2)
        if imc < 18.5:
            print("Abaixo do peso!!!")
        elif imc < 25:
            print("Normal!")
        elif imc < 30:
            print("Sobrepeso.")
        elif imc > 30: 
            print("Obesidade!!")
    elif atividade == 3:
        cpf = int(input("insira os numeros do seu cpf: \n"))
        if len(cpf) == 11:
            print("CPF valido.")
        else: 
            print("CPF invalido.")

    elif atividade == 4:
        numero = int(input("Insira um numero."))
        if numero%2 == 0 and numero%3 == 0:
            print("numero é par e multiplo de 3")
        elif numero % 2 == 0 :
            print("numero é par.")
        elif numero % 3 == 0 :
            print("Numero é divisivel por 3")
        else: 
            print("numero não é divisivel por 3 nem par,")

    elif atividade == 5:
        idade = int(input("Digite a sua idade: "))
        if idade < 12:
            print("Criança")
        elif idade <18 : 
            print("Adolescente")
        elif idade < 60 : 
            print("adulto")
        elif idade >= 60:
            print("Idoso")

    elif atividade == 6:
        caracter = input("Digite um caractere")
        if len(caracter) == 1:
            if caracter.isalpha and caracter.isupper:
                print("Letra maiuscula.")
            elif caracter.isalpha and caracter.islower:
                print("Letra minuscula.")
            else:
                print("Não é letra")     

    elif atividade == 7:
        acesso = int(input("Qual o seu nivel de acesso?\n (1 = admin ,2 = usuario, 3 = visitante.)\n"))
        if acesso == 1:
            print("Seja bem vindo senhor administrado do grupo.")
        elif acesso == 2:
            print("Seja bem vindo seu usuario.")
        elif acesso == 3:
            print("Seja bem vindo turista.")
        else: 
            print("acesso invalido")
    elif atividade == 8:
        hora = int(input("Digite as horas atual"))
        minutos = int(input("Digite o minuto"))
        # terminar
    print("CABOU! (press enter to choose another question.)")
