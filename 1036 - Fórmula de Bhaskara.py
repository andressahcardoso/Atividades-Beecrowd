import math

entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

Delta = ((B * B) - ( 4 * A * C))

if Delta < 0:
  print("Impossivel calcular")

if A == 0:
  print("Impossivel calcular")

if  A > 0 and Delta > 0:
  
  Delta2 = math.sqrt(Delta)

  Divisao = ((-B) + Delta2)
  Divisao2 = ((-B) - Delta2)

  R1 = Divisao / (2 * A)
  R2 = Divisao2 / (2 * A)

  print("R1 = %0.5f" %R1)
  print("R2 = %0.5f" %R2)