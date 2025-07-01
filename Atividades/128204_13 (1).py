#📌 1. for loop — estrutura básica

# Exemplo de loop for com uma lista
sequencia = ["maçã", "banana", "laranja"]

for item in sequencia:
    print(item)

#📌 2. for loop — com lista

# Exibindo os números de uma lista
numeros = [10, 20, 30, 40, 50]

for numero in numeros:
    print(numero)

#📌 3. for loop — com range()

# Usando range para repetir um loop 5 vezes
for i in range(5):  # Vai de 0 a 4
    print(i)

#📌 4. while loop — estrutura básica

# Exemplo básico de loop while
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1

#📌 5. break e continue

# Usando break e continue dentro de um loop
for i in range(10):
    if i == 5:
        break  # Interrompe o loop quando i for igual a 5
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)

#📌 6. else com loop for

# Exemplo de else após um loop for
for i in range(3):
    print(i)
else:
    print("Loop for concluído")

#📌 7. else com loop while

# Exemplo de else com loop while
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("Loop while concluído")

#📌 8. Comparando quando usar for e while

# for: quando sei quantas vezes quero repetir
for i in range(3):
    print("for:", i)

# while: quando depende de uma condição
resposta = ""
while resposta != "ok":
    resposta = input("Digite 'ok' para continuar: ")
print("Obrigado!")

