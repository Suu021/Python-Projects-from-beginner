def gerador_senha (key):
    import secrets
    import string

    todos_caract = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    codigo = ''.join(secrets.choice(todos_caract) for _ in range(key))
    return codigo

num = int(input("Digite o número de caracteres que deseja pra sua senha: "))
senha = gerador_senha(num)
print("Sua nova senha é: ", senha)


