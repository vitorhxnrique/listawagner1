letra = input("digite uma letra apenas: ")

while len(letra) > 1:
    print("digite APENAS UMA letra")
    letra = input("digite uma letra apenas: ")

if letra in 'aAeEiIoOuU':
    print("vogal")
else:
    print("consoante")

