while True:
    print("=-=" * 20)
    num = int(input("Quer ver a tabuada de qual valor? (negativo para parar) "))
    print("=-=" * 20)
    if num < 0:
        break
    c = 0
    multiplicador = 1

    while c < 10:
        tabuada = num * multiplicador
        print(f"{num} * {multiplicador} = {tabuada}")
        c += 1
        multiplicador += 1
print("Saindo...")