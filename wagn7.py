criminalidade = 0

pergunta1 = input("Telefonou para a vítima? (Responda com True ou False): ")
if pergunta1 == "True" or pergunta1 == "true":
    criminalidade += 1
pergunta2 = input("Esteve no local do crime? (Responda com True ou False): ")
if pergunta2 == "True" or pergunta2 == "true":
    criminalidade += 1
pergunta3 = input("Mora perto da vitima? (Responda com True ou False): ")
if pergunta3 == "True" or pergunta3 == "true":
    criminalidade += 1
pergunta4 = input("Devia para a vitima? (Responda com True ou False): ")
if pergunta4 == "True" or pergunta4 == "true":
    criminalidade += 1
pergunta5 = input("Ja trabalhou com a vitima? (Responda com True ou False): ")
if pergunta5 == "True" or pergunta5 == "true":
    criminalidade += 1



if criminalidade == 5:
    print("Assassino")
elif criminalidade == 3 or criminalidade == 4:
    print("Cumplice")
elif criminalidade == 2:
    print("Suspeito")
else:
    print("Inocente")