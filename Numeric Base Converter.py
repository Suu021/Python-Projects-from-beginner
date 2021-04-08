from colorama import Fore

def binary(num):
    list_b = []
    while num >= 2:
        div = num % 2
        list_b.append(str(div))
        n_bin = "".join(list_b)
        num = num // 2
    list_b.append(str(num))
    n_bin = "".join(list_b)
    return n_bin[::-1]


def octal(num):
    list_oc = []
    while num >= 8:
        div = num % 8
        list_oc.append(str(div))
        octal = "".join(list_oc)
        num = num // 8
    list_oc.append(str(num))
    octal = "".join(list_oc)
    return octal[::-1]


def hex(num):
    list_hex = []
    while num >= 16:
        div = num % 16
        if 15 >= div >= 10:
            dic_hexa = {
                "10": "A",
                "11": "B",
                "12": "C",
                "13": "D",
                "14": "E",
                "15": "F"
            }
            div = str(div)
            div = dic_hexa[div]
        list_hex.append(str(div))
        hex = "".join(list_hex)
        num = num // 16
    list_hex.append(str(num))
    hex = "".join(list_hex)
    return hex[::-1]


print("=-" * 20)
print(f"{'BASE CONVERTER':^39}")
print("=-" * 20)

while True:
    print("Menu:"
          "\nB - Decimal to Binary;"
          "\nO - Decimal to Octal;"
          "\nH - Decimal to Hexadecimal;"
          "\nE - To exit.")
    print("=-" * 20)
    menu = input(str("Which system do you want to convert to? ")).strip().upper()[0]
    while menu not in "BOHE":
        print(Fore.RED + f"Invalid option! Please, try again..." + Fore.RESET)
        menu = input(str("Which system do you want to convert to? ")).strip().upper()[0]

    num = int(input("Input your value: "))
    print("--" * 20)

    if menu == "B":
        print(Fore.BLUE + f"The binary conversion of {num} is {binary(num)}" + Fore.RESET)
        print("--" * 20)
    elif menu == "O":
        print(Fore.BLUE + f"The octal conversion of {num} is {octal(num)}" + Fore.RESET)
        print("--" * 20)
    elif menu == "H":
        print(Fore.BLUE + f"The hexadecinal conversion of {num} is {hex(num)}" + Fore.RESET)
        print("--" * 20)
    elif menu == "E":
        print("check back often")
        break
