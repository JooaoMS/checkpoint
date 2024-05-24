itens_mao = ["pano de prato", "copos", "fósforo"]
itens_carrinho = ["copos"]

itens_mao = list(set(itens_mao) - set(itens_carrinho))

print("Itens na mão:", itens_mao)
