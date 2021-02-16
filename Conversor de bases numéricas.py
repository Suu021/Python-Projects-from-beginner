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
    print(octal[::-1])

num = int(input("Qual número quer converter? "))
menu = input("Menu:"
              "\n(a)Binário;"
              "\n(b)octal;"
             "\npara qual sistema deseja converter? ")

if menu is "a":
    print(binario(num))
elif menu is "b":
    print(octal(num))
else:
    print("Opção inválida!")
