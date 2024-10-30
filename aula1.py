nome = input('Seu nome: ')
idade = input("Sua idade: ")
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido {nome[::-1]}')
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A ultima letra do seu nome é {nome[4::]}")
else:
    print('Faltou preencher algum campo!')

    