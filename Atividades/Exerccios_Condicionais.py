# =============================================
# EXERCÍCIOS DE PYTHON - CONDICIONAIS (IF, ELIF, ELSE)
# (Somente enunciados)
# =============================================
while True:
    atividade = int(input("Digite o número da atividade (1-20) (0 sai): "))
    if atividade == 0:
        break
    # === BÁSICOS ===
    # 1. Verificador de idade:
    #    Peça a idade do usuário e imprima "Maior de idade" ou "Menor de idade".
    elif atividade == 1:
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade")

    # 2. Positivo/Negativo/Zero:
    #    Peça um número e diga se é positivo, negativo ou zero.
    elif atividade == 2:
        numero = float(input("Digite um número: "))
        if numero > 0:
            print("Positivo")
        elif numero < 0:
            print("Negativo")
        else:
            print("Zero")
    # 3. Par ou Ímpar:
    #    Verifique se um número é par ou ímpar.
    elif atividade == 3:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("Par")
        else:
            print("Ímpar")        
    # 4. Acesso com senha:
    #    Crie uma senha fixa (ex: "python123"). Peça ao usuário para digitar a senha e informe se está correta ou não.
    elif atividade == 4:
        senha_usuario = input("Digite a senha: ")
        if senha_usuario == "Eduardo123":
            print("Senha correta")
        else:
            print("Senha incorreta")
    # 5. Múltiplo de 5:
    #    Verifique se um número é múltiplo de 5.
    elif atividade == 5:
        numero = int(input("Digite um número: "))
        if numero % 5 == 0:
            print("É múltiplo de 5")
        else:
            print("Não é múltiplo de 5")
    # 6. Dia da semana:
    #    Peça um número de 1 a 7 e imprima o dia correspondente (ex: 1 = Domingo).
    if atividade == 6:
        dia = int(input("Digite um número de 1 a 7: "))
        if dia == 1:
            print("Domingo")
        elif dia == 2:
            print("Segunda-feira")
        elif dia == 3:
            print("Terça-feira")
        elif dia == 4:
            print("Quarta-feira")
        elif dia == 5:
            print("Quinta-feira")
        elif dia == 6:
            print("Sexta-feira")
        elif dia == 7:
            print("Sábado")
        else:
            print("Número inválido, insira um numero de 1 a 7")
    # 7. Maior entre 3 números:
    #    Peça três números e mostre o maior deles.
    elif atividade == 7:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        maior = max(num1, num2, num3)
        print(f"O maior número é: {maior}")   
    # 8. Aprovação:
    #    Peça uma nota (0 a 10) e diga "Aprovado" (≥7) ou "Reprovado".
    elif atividade == 8:
        media = int(input("Digite uma nota (0 a 10): "))
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
    # === INTERMEDIÁRIOS ===
    # 9. Triângulo:
    #    Peça 3 lados e verifique se formam um triângulo válido.
    elif atividade == 9:
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        if lado1 == lado2 == lado3:
            print("O triangulo é equilatero")
        elif lado1 == lado2 and lado2 != lado3 or lado3 == lado2 and lado1 != lado3:
            print("O triangulo é isóceles.")
        else:
            print("O triangulo é escaleno") 
    # 10. Desconto para idosos/estudantes:
    #     Peça idade e se é estudante (S/N). Dê 20% de desconto para idosos (≥60) OU estudantes.
    elif atividade == 10:
        idade = int(input("Digite sua idade: "))
        estudante = input("Você é estudante? (S/N): ").strip().upper()
        if idade >= 60 or estudante == 'S':
            print("Você tem direito a 20% de desconto")
        else:
            print("Você não tem direito a desconto")
    # 11. Turno do dia:
    #     Peça um horário (ex: 14) e classifique em Manhã (6-12), Tarde (13-18), Noite (19-23).
    elif atividade == 11:
        horario = int(input("Digite um horário (0-23): "))
        if 6 <= horario <= 12:
            print("Bom dia!")
        elif 13 <= horario <= 18:
            print("Boa tarde!")
        elif 19 <= horario < 24:
            print("Boa noite!")
    # 12. Ano bissexto:
    #     Verifique se um ano é bissexto (pesquise as regras).
    elif atividade == 12:
        ano = int(input("Digite o ano que você quer verificar. "))   
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            print('Ano bissexto.')
        else:
            print('Não é um ano bissexto.')
    # 13. Categoria de filme:
    #     Peça a idade e classifique: "Livre" (todas), "12+" (≥12), "18+" (≥18).
    elif atividade == 13:
        idade = int(input("Qual a idade recomendada do filme?"))
        if idade <=12:
            print("Livre.")
        elif idade >12:
            print("12+")
        else:
            print("18+")
    # 14. Login e senha:
    #     Valide usuário ("admin") e senha ("1234").
    elif atividade == 14:
        usuario = input("Digite o usuario: ")
        senha = input("Digite a senha: ")
        if usuario == "admin" and senha == "1234":
            print("Acesso liberado")
        else: 
            print("Acesso negado")
    # 15. Número positivo e par:
    #     Verifique se um número é positivo E par.
    elif atividade == 15:
        numero = int(input("Insira um numero"))
        if numero>0 and numero%2 == 0:
            print("Numero é positivo e par.")
        else:
            print("O numero não é positivo e par.")
    # === AVANÇADOS ===
    # 16. Caixa eletrônico:
    #     Simule um saque bancário (saldo=1000). Verifique se o valor é válido (não negativo e ≤ saldo).
    elif atividade == 16:
        saldo = 1000
        saque = int(input("Quantos você quer sacar?"))
        if saque < 1000 and saque > 0:
            print("SAQUE FEITO!!!") 
        else:
            print("Você nao pode sacar essa quantia.")
    # 17. Plano de internet:
    #     Calcule o custo de uso: R$50 para até 10GB, R$7/GB adicional.
    elif atividade == 17:
        gb = int(input("Quantos GB você usou?"))
        if gb <= 10:
            print("Seu plano é de 50 reais.")
        else:
            adicional = (gb - 10) * 7
            total = 50 + adicional
            print(f"Seu plano é de {total} reais.")
    # 18. Aumento salarial:
    #     Peça salário e tempo de empresa. Dê 10% de aumento se tempo ≥5 anos, senão 5%.
    elif atividade == 18:
        salario = float(input("Digite seu salário: "))
        tempo_empresa = int(input("Há quantos anos você trabalha na empresa? "))
        if tempo_empresa >= 5:
            novo_salario = salario * 1.10
        else:
            novo_salario = salario * 1.05
        print(f"Seu novo salário é: {novo_salario:.2f}")
    # 19. Verificador de vogal:
    #     Peça uma letra e diga se é vogal (a, e, i, o, u).
    elif atividade == 19:
        letra = input("Digite uma letra: ")
        if letra in 'aeiou':
            print("É uma vogal.")
        else:
            print("Não é uma vogal.")
    # 20. Divisível por 3 e 5:
    #     Verifique se um número é divisível por 3 E 5 simultaneamente.
    elif atividade == 20:
        numero = int(input("Digite um número: "))
        if numero % 3 == 0 and numero % 5 == 0:
            print("O número é divisível por 3 e 5.")
        else:
            print("O número não é divisível por 3 e 5.")
    else:
        print("Atividade inválida. Tente novamente.")