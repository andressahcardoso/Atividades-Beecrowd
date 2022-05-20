Idade = int(input())

Anos = int(Idade / 365)

Mes = int((Idade - 365 * Anos) / 30)

Dias = int((Idade - 365 * Anos) - Mes * 30)

print(Anos,"ano(s)")
print(Mes,"mes(es)")
print(Dias,"dia(s)")
