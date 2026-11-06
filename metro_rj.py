import networkx as nx
 
LINHAS = {
    "Linha 1": [
        "Uruguai", "Saens Peña", "São Francisco Xavier", "Afonso Pena",
        "Estácio", "Praça Onze", "Central do Brasil",
        "Saara / Presidente Vargas", "Uruguaiana", "Carioca", "Cinelândia",
        "Glória", "Catete", "Largo do Machado", "Flamengo", "Botafogo",
        "Cardeal Arcoverde", "Siqueira Campos", "Cantagalo", "General Osório",
    ],
    "Linha 2": [
        "Pavuna", "Engenheiro Rubens Paiva", "Acari / Fazenda Botafogo",
        "Coelho Neto", "Colégio", "Irajá", "Vicente de Carvalho",
        "Thomaz Coelho", "Engenho da Rainha", "Inhaúma", "Del Castilho",
        "Maria da Graça", "Triagem", "Rei Pelé / Maracanã", "São Cristóvão",
        "Cidade Nova", "Central do Brasil",
        "Saara / Presidente Vargas", "Uruguaiana", "Carioca", "Cinelândia",
        "Glória", "Catete", "Largo do Machado", "Flamengo", "Botafogo",
    ],
    "Linha 4": [
        "Jardim Oceânico", "São Conrado", "Antero de Quental",
        "Jardim de Alah", "Nossa Senhora da Paz", "General Osório",
    ],
}


def construir_grafo(linhas):
    G = nx.Graph()

    for nome, estacoes in linhas.items():
        for i in range(len(estacoes) - 1):
            u = estacoes[i]
            v = estacoes[i + 1]
            if G.has_edge(u, v):
                G[u][v]['linhas'].add(nome)
            else:
                G.add_edge(u, v, linhas={nome})

    return G

G = construir_grafo(LINHAS)
print(G)