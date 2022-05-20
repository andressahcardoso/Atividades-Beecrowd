entrada = input().split()

A = int(entrada[0]) 
B = int(entrada[1])
C = int(entrada[2])


ordem = (sorted( [A, B, C]))

print (*ordem, sep='\n')

print()

print(A)
print(B)
print(C)