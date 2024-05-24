while True:
    quantidade_pessoas = int(input("Quantas pessoas estarão na sua reunião? "))
    if quantidade_pessoas <= 25:
        break
    print("Desculpe, o limite de pessoas é de 25. Por favor, ajuste a lista.")


convidados = ["João"]


for i in range(quantidade_pessoas - 1):
    nome = input(f"Nome do convidado {i+1}: ")
    convidados.append(nome)


print("\nLista de Convidados:")
for convidado in convidados:
    print(convidado)
