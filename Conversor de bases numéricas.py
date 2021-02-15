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


num = int(input("Qual número quer converter? "))
print(binario(num))
