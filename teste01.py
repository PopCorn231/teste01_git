def calcular_media_boletim(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcular_media_boletim(nota1, nota2, nota3, nota4)
print(f"A média do seu boletim foi: {media}")
