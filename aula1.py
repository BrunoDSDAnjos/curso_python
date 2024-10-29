entrada = input('[E]ntrada [S]air: ')
senha_digitada = int(input('Senha: '))
senha_permitida = 88724533
if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print('Bem vindo')
else:
    print('Senha invalida')