num_participantes = 5

nomes = []
pontuacoes = []

for i in range(num_participantes):
    nome = input("Nome do participante: ")
    pontuacao = float(input("Pontuação do participante: "))
    nomes.append(nome)
    pontuacoes.append(pontuacao)

maior_pontuacao = max(pontuacoes)
menor_pontuacao = min(pontuacoes)
pontuacao_media = sum(pontuacoes) / num_participantes

print("Maior pontuação:", maior_pontuacao)
print("Menor pontuação:", menor_pontuacao)
print("Pontuação média:", pontuacao_media)
