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
        if hora <= 24 and minutos <=60:
            print(f"Horario valido, são {hora}:{minutos}")
        else:
            print("Horario invalido")
    elif atividade == 9:
        numero = int(input("Insira um numero entre 100 a 200. "))
        if numero >= 100 and numero <=200:
            print("numero na faixa correta.")
        else: 
            print("Faixa de numero errada.")
    elif atividade == 10:
        numero1 = int(input("Insira um numero. "))
        numero2 = int(input("Insira outro numero. "))
        if numero1 > 0 and numero2 >0:
            print(numero1 + numero2)
        else:
            print(numero1 - numero2)

    elif atividade == 11:
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        if lado1 == lado2 == lado3:
            print("O triangulo é equilatero")
        elif lado1 == lado2 and lado2 != lado3 or lado3 == lado2 and lado1 != lado3:
            print("O triangulo é isóceles.")
        else:
            print("O triangulo é escaleno") 
    
    elif atividade == 12:
        operador = input("Qual operador quer usar para a conta? (+, - , *, /) ")
        numero1 = int(input("Insira um numero. "))
        numero2 = int(input("Insira outro numero. "))
        if operador == "+":
            print(numero1+numero2)
        elif operador == "-":
            print(numero1 - numero2)
        elif operador == "*":
            print(numero1 * numero2)
        elif operador == "/":
            print(numero1/ numero2)
        else:
            print("Operador invalido")
    elif atividade == 13:
        while True:
            nota1 = float(input("Insira a 1ª nota. "))
            nota2 = float(input("Insira a 2ª nota. "))
            if (nota1+nota2)/2 >= 7:
                print("Você esta aprovado!!")
                break
            elif (nota1+nota2)/2 >= 4:
                print("Voce ficou de recuperção. cuidado.")
            else: 
                print("Reprovado")
                break

    elif atividade == 14:
        i=0
        while i!=2:
            usuario = input("Insira o usuario.")
            senha = input("Insira a senha. ")
            if senha == "admin" and usuario == "admin":
                print("Acesso aprovado.")
                break
            else:
                print(f"Senha e/ou usuario invalido, tente novamente, você tem {3-i} tentativas restantes.")
                i+=1
            if i == 3:
                print("Você atingiu o limite de tentativas")
    elif atividade == 15:
        usoEnergia = float(input("Qual o seu uso energitico? (em kWh)\n"))
        if usoEnergia < 100:
            valor = usoEnergia * 0.5
        elif usoEnergia <=200:
            valor = usoEnergia*0.7
        elif usoEnergia > 200:
            valor = usoEnergia * 0.9
        print(f"O valor da conta de energia foi de {valor}")

    elif atividade == 16:
        valor = float(input("Qual o valor do produto? "))
        estado = input("De qual estado você é? ")
        if valor <= 300:
            if estado == "SC":
                print("Será 10 R$ de frete.")
            elif estado == "SP":
                print("Será 20R$ de frete.")
            elif estado == "RJ":
                print("Será 30 R$ de frete. ")
            else:
                print("Não enviamos para seu estado.")
        elif estado == "SC" or estado == "SP" or estado == "RJ":
            print("Não paga frete")
        else:
            print("Não enviamos para seu estado.")

    elif atividade == 17:
        renda = float(input("Insira a sua renda mensal. "))
        if renda < 2000:
            print("Isento de imposto de renda.")
        elif renda < 3500:
            print(f"Você tera que pagar {renda*0.075} R$ de imposto.")
        elif renda < 5000:
            print(f"Você tera que pagar {renda * 0.15}")
        else:
            print(f"Você tera que pagar {renda * 0.225}")
    print("CABOU! (press enter to choose another question.)")
