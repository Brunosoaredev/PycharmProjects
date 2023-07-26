# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em umas lista. Caso o número
# já exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# CRESCENTE.

números = list()

# Inicia o loop infinito.

while True:
    n = int(input('Digite um valor: '))
    if n not in números:

# Adiciona o valor na lista

        números.append(n)
        print('Valor adicionado com sucesso.')

# Valores duplicados serão ignorados.

    else:
        print('Valor duplicado! Não vou adicionar...')

# Resposta de [S/N] para o loop

    r = str(input('Quer continuar[S/N]: '))
    if r in 'Nn':
        break   # Finaliza o loop´
print('-=' * 30)

# Organiza a lista em ordem crescente

números.sort()
print(f'Você digitou os valores: {números}')
