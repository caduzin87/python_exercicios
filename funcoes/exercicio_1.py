def calcularMedia(nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

print('Calcular de Média')
n1 = float(input('Digite a 1ª '))
n2 = float(input('Digite a 2ª '))
n3 = float(input('Digite a 3ª '))
n4 = float(input('Digite a 4ª '))
m = calcularMedia(n1, n2, n3, n4)
print(f"Sua média é {m}")