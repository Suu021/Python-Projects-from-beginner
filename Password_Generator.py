from colorama import Fore


def generate_password(key=16):
    from secrets import choice
    import string

    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    code_c = ''.join(choice(all_characters) for _ in range(key))
    return code_c


print("=-" * 20)
print(f"{'Password Generator':^40}")
print("=-" * 20)
while True:
    num = input("How many characters do you want for your password: ")
    try:
        int(num)
    except (ValueError, KeyError):
        print(Fore.RED + f'Error! "{num}" it is not an integer. Please enter a integer.' + Fore.RESET)
        continue
    else:
        num = int(num)
        if num < 5:
            print(Fore.RED + f"Your password must be at least 4 characters long. Please try again." + Fore.RESET)
            continue
        break
print("--" * 20)
password = generate_password(num)
print(f"Your new password is: " + Fore.MAGENTA + f"{password}" + Fore.RESET)
print("--" * 20)
