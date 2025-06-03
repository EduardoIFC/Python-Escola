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
    # 10. Desconto para idosos/estudantes:
    #     Peça idade e se é estudante (S/N). Dê 20% de desconto para idosos (≥60) OU estudantes.
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        if lado1 == lado2 == lado3:
            print("Os lados formam um triângulo válido")
        else:
            print("Os lados não formam um triângulo válido")
    # 11. Turno do dia:
    #     Peça um horário (ex: 14) e classifique em Manhã (6-12), Tarde (13-18), Noite (19-23).

    # 12. Ano bissexto:
    #     Verifique se um ano é bissexto (pesquise as regras).

    # 13. Categoria de filme:
    #     Peça a idade e classifique: "Livre" (todas), "12+" (≥12), "18+" (≥18).

    # 14. Login e senha:
    #     Valide usuário ("admin") e senha ("1234").

    # 15. Número positivo e par:
    #     Verifique se um número é positivo E par.

    # === AVANÇADOS ===
    # 16. Caixa eletrônico:
    #     Simule um saque bancário (saldo=1000). Verifique se o valor é válido (não negativo e ≤ saldo).

    # 17. Plano de internet:
    #     Calcule o custo de uso: R$50 para até 10GB, R$7/GB adicional.

    # 18. Aumento salarial:
    #     Peça salário e tempo de empresa. Dê 10% de aumento se tempo ≥5 anos, senão 5%.

    # 19. Verificador de vogal:
    #     Peça uma letra e diga se é vogal (a, e, i, o, u).

    # 20. Divisível por 3 e 5:
    #     Verifique se um número é divisível por 3 E 5 simultaneamente.