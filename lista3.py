# Crie um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


listanum = []    # Lista numérica
mai = 0     # Contador do maior valor
men = 0     # contador do menor valor
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))

# Primeiro valor lido é o maior e o menor valor.

    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:    # Maior valor digitado na lista
            mai = listanum[c]
        if listanum[c] < men:    # Menor valor digitado na lista
            men = listanum[c]

# Valores numéricos digitados na lista

print(f'Você digitou os valores {listanum}')

# Posição do maior valor digitado na lista

print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()

# Posição do menor valor digitado na lista

print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        if v == men:
            print(f'{i}... ', end='')
print()
