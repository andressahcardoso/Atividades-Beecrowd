dentro = 0
fora= 0

N = int(input())

for i in range (0, N):
  X = int(input())

  if X >= 10 and X <= 20:
    dentro += 1

  else:
    fora += 1

print(dentro, "in") 
print(fora, "out")