def testador(key):
    import random
    import string

    todos_caract = string.ascii_uppercase+string.ascii_lowercase+string.digits
    num_letras = len(key)

    codigo = ''.join(random.choice(todos_caract) for _ in range(num_letras))
    while codigo != key:
        codigo = ''.join(random.choice(todos_caract) for _ in range(num_letras))
        if codigo == key:
            return codigo


def tempo_quebrar_senha(teste):
    from timeit import timeit

    tempo = timeit('teste', 'from __main__ import teste', number=1)
    return tempo


senha = input("Digite a senha que deseja testar: ")
teste = testador(senha)
tempo_teste = tempo_quebrar_senha(teste)
print(teste)
print("O keylogger levaria aproximadamente ", tempo_teste, "segundos pra quebrar a sua senha")
