"""
Tabela de correspondência: nome da seleção (dataset World Cup) -> código iso3 (dataset HDI).

Por que existe: o merge só junta chaves idênticas. O dataset de Copas usa nomes de
seleções ("West Germany", "England", "Soviet Union"), enquanto o HDI usa códigos de
países atuais. Sem esta tabela, essas seleções sumiriam da análise sem aviso.

Decisões (registrar na documentação técnica):
- Inglaterra, Escócia, País de Gales e Irlanda do Norte -> GBR (o HDI só tem o Reino Unido).
- Alemanha Ocidental (1990) -> DEU.
- União Soviética -> RUS; Tchecoslováquia -> CZE; Iugoslávia / Sérvia e Montenegro -> SRB.
- Coreia do Norte -> PRK, mas o HDI não tem dados dela: os jogos ficam sem renda.
Vários apelidos por país porque a grafia pode variar ("USA", "United States"...).
"""

import unicodedata

MAPA_ISO3 = {
    "Algeria": "DZA",
    "Angola": "AGO",
    "Argentina": "ARG",
    "Australia": "AUS",
    "Austria": "AUT",
    "Belgium": "BEL",
    "Bolivia": "BOL",
    "Bosnia and Herzegovina": "BIH",
    "Bosnia-Herzegovina": "BIH",
    "Brazil": "BRA",
    "Bulgaria": "BGR",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Chile": "CHL",
    "China": "CHN",
    "China PR": "CHN",
    "Colombia": "COL",
    "Costa Rica": "CRI",
    "Croatia": "HRV",
    "Czech Republic": "CZE",
    "Czechia": "CZE",
    "Czechoslovakia": "CZE",
    "Denmark": "DNK",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "England": "GBR",
    "France": "FRA",
    "Germany": "DEU",
    "West Germany": "DEU",
    "Germany FR": "DEU",
    "Ghana": "GHA",
    "Greece": "GRC",
    "Honduras": "HND",
    "Iceland": "ISL",
    "Iran": "IRN",
    "IR Iran": "IRN",
    "Republic of Ireland": "IRL",
    "Ireland": "IRL",
    "Italy": "ITA",
    "Ivory Coast": "CIV",
    "Cote d'Ivoire": "CIV",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Mexico": "MEX",
    "Morocco": "MAR",
    "Netherlands": "NLD",
    "New Zealand": "NZL",
    "Nigeria": "NGA",
    "North Korea": "PRK",
    "Korea DPR": "PRK",
    "Northern Ireland": "GBR",
    "Norway": "NOR",
    "Panama": "PAN",
    "Paraguay": "PRY",
    "Peru": "PER",
    "Poland": "POL",
    "Portugal": "PRT",
    "Qatar": "QAT",
    "Romania": "ROU",
    "Russia": "RUS",
    "Soviet Union": "RUS",
    "USSR": "RUS",
    "Saudi Arabia": "SAU",
    "Scotland": "GBR",
    "Senegal": "SEN",
    "Serbia": "SRB",
    "Serbia and Montenegro": "SRB",
    "Yugoslavia": "SRB",
    "FR Yugoslavia": "SRB",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "South Africa": "ZAF",
    "South Korea": "KOR",
    "Korea Republic": "KOR",
    "Spain": "ESP",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Togo": "TGO",
    "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN",
    "Turkey": "TUR",
    "Ukraine": "UKR",
    "United Arab Emirates": "ARE",
    "United States": "USA",
    "USA": "USA",
    "Uruguay": "URY",
    "Wales": "GBR",
}


def sem_acentos(texto):
    """Remove acentos ("Côte" -> "Cote") para a busca não falhar por codificação."""
    return unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()


_MAPA_NORMALIZADO = {sem_acentos(k).lower(): v for k, v in MAPA_ISO3.items()}


def nome_para_iso3(nome):
    """Devolve o iso3 da seleção, ou None se o nome não estiver na tabela."""
    return _MAPA_NORMALIZADO.get(sem_acentos(nome).strip().lower())
