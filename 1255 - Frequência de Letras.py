numero_usuario = int(input())

n1 = 0
n2 = 1

print(n1, n2, end="") 

cont = 3  
while cont <= numero_usuario:  

    n3 = n1 + n2

    print(" {}" .format(n3), end="")
    
    n1 = n2
    n2 = n3
    
    cont += 1

print("")