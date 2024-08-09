turno = input("digite o turno em que estuda: M, V ou N  ")

while len(turno) > 1:
    print("Valor invalido  ")
    turno = input("digite o turno em que estuda: M, V ou N  ")

if turno in "Mm":
    print("Bom Dia")

elif turno in "Vv":
    print("Boa Tarde")

elif turno in "Nn":
    print("Boa Noite")