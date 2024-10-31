lista = []
while True == True:
    try:
        user = input('''Selecione uma opção
        [i]nserir [a]pagar [l]ista : ''')
        if user == 'l':
            indice = len(lista)
            for indice, user in enumerate(lista):
                print(indice, user)
        elif user == 'i':
            user_inserir = input('Digite o valor: ')
            lista.append(user_inserir)
        elif user == 'a':
            indice = len(lista)
            for indice, user in enumerate(lista):
                print(indice, user)
            user_apagar = int(input("Escolha qual indece apagar: "))
            lista.pop(user_apagar)
    except:
        print('Escolha uma opção valida')