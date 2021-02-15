def binario (num):
    lista_b = []
    while num >= 2:
        div = num % 2
        lista_b.append(str(div))
        bin = "".join(lista_b)
        num = num // 2
    lista_b.append(str(num))
    bin = "".join(lista_b)
    return bin[::-1]

num = int(input("Qual número quer converter? "))
print(binario(num))

