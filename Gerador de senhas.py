def gerador_senha (key):
    import random
    import string

    todos_caract = string.ascii_uppercase+string.ascii_lowercase+string.digits
    codigo = ''.join(random.choice(todos_caract) for _ in range(key))
    return codigo

num = int(input(print("Digite o número de caracteres que deseja pra sua senha: ")))
senha = gerador_senha(num)
print("Sua nova senha é: ", senha)
