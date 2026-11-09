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

COORD = {"Uruguai":(-22.9306950, -43.2378600), "Saens Peña":(-22.9244648, -43.2326678), 
         "São Francisco Xavier":(-22.9205275, -43.2237596), "Afonso Pena":(-22.9182105, -43.2179158),
         "Estácio":(-22.9135368, -43.2065707), "Praça Onze":(-22.9099170, -43.2002830),
         "Central do Brasil":(-22.9050384, -43.1907819), 
         "Saara / Presidente Vargas":(-22.9033410, -43.1861796),
         "Uruguaiana":(-22.9028932, -43.1817992), "Carioca":(-22.9028932, -43.1817992), 
         "Cinelândia":(-22.9108971, -43.1756798), "Glória":(-22.9206347, -43.1766221), 
         "Catete":(-22.9259549, -43.1765501), "Largo do Machado":(-22.9311351, -43.1776774), 
         "Flamengo":(-22.9371801, -43.1785394), "Botafogo":(-22.9503653, -43.1842007),
         "Cardeal Arcoverde":(-22.9638248, -43.1813721), "Siqueira Campos":(-22.9673066, -43.1873375),
         "Cantagalo":(-22.9754882, -43.1944571), "General Osório":(-22.9821162, -43.1964357), 
         "Pavuna":(-22.8063182, -43.3654752), "Engenheiro Rubens Paiva":(-22.8162957, -43.3584824),
         "Acari / Fazenda Botafogo":(-22.8249975, -43.3493019), "Coelho Neto":(-22.8318735, -43.3429193),
         "Colégio":(-22.8426601, -43.3345459), "Irajá":(-22.8480227, -43.3232651), 
         "Vicente de Carvalho":(-22.8540406, -43.3131537), "Thomaz Coelho":(-22.8626005, -43.3067943),
         "Engenho da Rainha":(-22.8679238, -43.2973765), "Inhaúma":(-22.8745685, -43.2834559), 
         "Del Castilho":(-22.8792762, -43.2719274), "Maria da Graça":(-22.8814941, -43.2601882), 
         "Triagem":(-22.8967174, -43.2440972), "Rei Pelé / Maracanã":(-22.9097160, -43.2338900),
         "São Cristóvão":(-22.9096934, -43.2209945), "Cidade Nova":(-22.9087465, -43.2062984), 
         "Jardim Oceânico":(-23.0068340, -43.3109619), "São Conrado":(-22.9912296, -43.2550269), 
         "Antero de Quental":(-22,9845429, -43.2236274), "Jardim de Alah":(-22.9837348, -43.2162656),
         "Nossa Senhora da Paz":(-22.9837208, -43.2060232)}

print(len(COORD))