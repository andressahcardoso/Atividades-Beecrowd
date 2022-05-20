notas = input().split()

N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print("Media: %0.1f" %media)

if media >= 7:
    print("Aluno aprovado.")
    
elif media < 5:
    print("Aluno reprovado.")
    
if media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    
    Nota_exame = float(input())
    
    print("Nota do exame: %0.1f" %Nota_exame)
    
    media = (media + Nota_exame) / 2

    if media >= 5:
        print("Aluno aprovado.")
        
    else:
        print("Aluno reprovado.")
        
    print("Media final: %0.1f" %media)