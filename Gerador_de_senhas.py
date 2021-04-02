from colorama import Fore

def gerador_senha(key):
    from secrets import choice
    import string

    todos_caracteres = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    codigo = ''.join(choice(todos_caracteres) for _ in range(key))
    return codigo

print("=-" * 20)
print(f"{'Gerador de senhas':^40}")
print("=-" * 20)

num = int(input("Quantos caracteres você quer pra sua senha: "))
print("--" * 20)
senha = gerador_senha(num)
print(f"Sua nova senha é: " + Fore.MAGENTA + f"{senha}" + Fore.RESET)
print("--" * 20)


