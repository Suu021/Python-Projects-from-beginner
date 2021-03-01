def binario(num):
    lista_b = []
    while num >= 2:
        div = num % 2
        lista_b.append(str(div))
        n_bin = "".join(lista_b)
        num = num // 2
    lista_b.append(str(num))
    n_bin = "".join(lista_b)
    return n_bin[::-1]

def octal(num):
    lista_oc = []
    while num >= 8:
        div = num % 8
        lista_oc.append(str(div))
        octal = "".join(lista_oc)
        num = num // 8
    lista_oc.append(str(num))
    octal = "".join(lista_oc)
    return octal[::-1]

def hex(num):
    lista_hex = []
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
        lista_hex.append(str(div))
        hex = "".join(lista_hex)
        num = num // 16
    lista_hex.append(str(num))
    hex = "".join(lista_hex)
    return hex[::-1]

sair = False
while not sair:
    menu = input("Menu:"
                  "\n(a)Binário;"
                  "\n(b)Octal;"
                  "\n(c)Hexadecimal;"
                  "\nQualquer outra tecla para sair."
                  "\nPara qual sistema deseja converter o número decimal? ").strip().lower()

    if menu == "a":
        num = int(input("Qual valor quer converter? "))
        print(binario(num))
    elif menu == "b":
        num = int(input("Qual valor quer converter? "))
        print(octal(num))
    elif menu == "c":
        num = int(input("Qual valor quer converter? "))
        print(hex(num))
    else:
        print("Saindo...")
        sair = True
