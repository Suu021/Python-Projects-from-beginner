def gerador_senha (key):
    import random
    import string

    todos_caract = string.ascii_uppercase+string.ascii_lowercase+string.digits
    codigo = ''.join(random.choice(todos_caract) for _ in range(key))
    return codigo

str = input(print("Digite o número de caracteres que deseja pra sua senha: "))
num= int(str)
senha = gerador_senha(num)
print("Sua nova senha é: ", senha)
