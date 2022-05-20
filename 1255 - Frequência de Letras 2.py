n = int(input())

for i in range(0,n):
  s = input()
  s = s.lower()
  letras = {}
  max = 0
  
  for j in range(0, len(s)):
    if s[j] != ' ' and s[j].isalpha() == 1:
      if s[j] in letras:
        letras[s[j]] += 1
      else: 
        letras[s[j]] = 0

  letras = dict(sorted(letras.items()))

  saida = ''

  for key, value in letras.items():
    if value > max:
      max = value

  for key, value in letras.items():
    if value == max:
      saida += key

  print(saida)

# Código prof. Felipe