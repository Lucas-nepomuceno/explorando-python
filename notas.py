from tempo import calcula_media

notas = []
for i in range(1, 4):
    notas.append(float(input(f"Digite a {i}a nota: ")))

media = round(calcula_media(notas),2)
if __name__ =="__main__":
    if media == 10:
        print("Aprovado com distinção")
    elif (media < 10) & (media >= 7):
        print("Aprovado")
    else:
        print("Reprovado") 
