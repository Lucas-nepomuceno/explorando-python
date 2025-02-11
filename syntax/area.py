import math
from teste_importacao import main

#Enter the triangle's sides
a = float(input("Primeiro Lado: "))
b = float(input("Segundo Lado: "))
c = float(input("Terceiro Lado: "))
lados = [a,b,c]

def calcula_area(lados):
	semiperimetro = sum(lados)/2
	soma_raiz = semiperimetro
	for lado in lados:
		soma_raiz = soma_raiz * (semiperimetro - lado)
	return math.sqrt(soma_raiz)

print(calcula_area(lados))

print("==============")
print("Testando importação de módulo")
main()