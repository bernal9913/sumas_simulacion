def sumcli(a, b) -> None:
    total = a + b
    print('Total: %s'%(total))

if __name__ == "__main__":
    print("Sumatoria cli")
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese otro numero: "))
    sumcli(a, b)