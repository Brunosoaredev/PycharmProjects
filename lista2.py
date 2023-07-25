valores = list()

for cont in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}!')
print(f'O maior valor foi {max(valores)} ', end='')
print(f'e o menor valor foi {min(valores)}.')