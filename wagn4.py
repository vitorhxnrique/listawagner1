nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
media = 0

media = (nota1 + nota2) / 2

while media > 10:
    nota1 = float(input("digite a nota 1: "))
    nota2 = float(input("digite a nota 2: "))
    media = 0

    media = (nota1 + nota2) / 2

if media == 10:
    print("aprovado com distincao")
elif media >= 7:
    print("aprovado")
else:
    print("reprovado")
