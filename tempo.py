medicoes = []

for i in range(1, 16):
	medicoes.append(float(input(str(i) + "a medição: ")))

calcula_media = lambda x: sum(x)/len(x)

medicoes.sort()

print("Tempo Máximo: ", medicoes[-1])
print("Tempo Mínimo: ", medicoes[0])
print("Tempo Médio: ", calcula_media(medicoes))
print(sum(medicoes))
print(len(medicoes))



 