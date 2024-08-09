numero1 = int(input("digite primeiro numero "))
numero2 = int(input("digite segundo numero "))
numero3 = int(input("digite terceiro numero "))

if numero1 > numero2 and numero1 > numero3:
    print("o maior numero e " + str(numero1) + ".")
elif numero2 > numero1 and numero2 > numero3:
    print("o maior numero e " + str(numero2) + ".")
else:
    print("o maior numero e " + str(numero3) + ".")