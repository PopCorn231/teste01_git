def calcular_media_boletim(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

name = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcular_media_boletim(nota1, nota2, nota3, nota4)
print(f"A média do seu boletim foi: {media}")

if media > 6:
    print("Você foi aprovado!")
elif media == 6:
    print("Você está de recuperação")
else:
    print("Você foi reprovado!")

print(f'Seu nome é {name} sua idade é {idade}')