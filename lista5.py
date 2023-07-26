# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (Sem usar o sort() ).No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):   # ler 5 valores  lembrando que o último valor é desconsiderado.
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:   # Vai dar o append se for o primeiro valor da lista ou o último valor da lista.
        lista.append(n)  # Adiciona o valor digitado no final da lista.
        print('Adicionado no final da lista...')
    else:
        pos = 0

        while pos < len(lista):  # Posição da lista 0 até a útima posição.
            if pos <= lista[pos]:
                lista.insert(pos, n)  # Insere o valor especificado na posição especificada .
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram {lista}')





