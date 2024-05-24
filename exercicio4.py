# Número fixo de participantes
num_participantes = 5

# Listas para armazenar nomes e pontuações
nomes = []
pontuacoes = []

# Loop para entrada de dados
for i in range(num_participantes):
    nome = input("Nome do participante: ")
    pontuacao = float(input("Pontuação do participante: "))
    nomes.append(nome)
    pontuacoes.append(pontuacao)

# Calcula maior pontuação, menor pontuação e pontuação média
maior_pontuacao = max(pontuacoes)
menor_pontuacao = min(pontuacoes)
pontuacao_media = sum(pontuacoes) / num_participantes

# Exibe os resultados
print("Maior pontuação:", maior_pontuacao)
print("Menor pontuação:", menor_pontuacao)
print("Pontuação média:", pontuacao_media)
