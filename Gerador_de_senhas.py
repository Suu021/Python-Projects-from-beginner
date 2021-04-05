from colorama import Fore


def gerar_senha(key=16):
    from secrets import choice
    import string

    todos_caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    codigo = ''.join(choice(todos_caracteres) for _ in range(key))
    return codigo


print("=-" * 20)
print(f"{'Gerador de senhas':^40}")
print("=-" * 20)
while True:
    num = input("Quantos caracteres você quer pra sua senha: ")
    try:
        int(num)
    except (ValueError, KeyError):
        print(Fore.RED + f'Erro! "{num}" não é um número inteiro. Por favor, digite um número inteiro.' + Fore.RESET)
        continue
    else:
        num = int(num)
        if num < 5:
            print(Fore.RED + f"Sua senha precisa ter ao menos 4 caracteres. Por favor, tente de novo." + Fore.RESET)
            continue
        break
print("--" * 20)
senha = gerar_senha(num)
print(f"Sua nova senha é: " + Fore.MAGENTA + f"{senha}" + Fore.RESET)
print("--" * 20)
