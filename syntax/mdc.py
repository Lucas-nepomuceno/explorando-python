def calcula_mdc(numeros:list):
    resto = -1
    a = numeros[1]
    b = numeros[0]
    while (resto != 0):
        resto = a % b
        a = b
        b = resto
    return (a)

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
numeros = [a,b]
numeros.sort()
print(calcula_mdc(numeros))