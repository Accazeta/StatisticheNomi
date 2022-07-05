import matplotlib.pyplot as plt

from filtertype import filterType
import matplotlib.pyplot as ppl


def check_available_years(ws):
    lista_anni = []
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[0].value not in lista_anni:
            lista_anni.append(row[0].value)
    return lista_anni


def check_missing_years(lista_anni):
    lista_anni.sort()
    gap_years = []
    year = lista_anni[0]
    while year != lista_anni[-1]:
        if year + 1 not in lista_anni:
            gap_years.append(year + 1)
        year = year + 1


def somma_nuovi_nati(ws, filtro, filter_type):
    somma = 0
    match filter_type:
        case filterType.ANNO:  # caso anno di nascita
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
                if row[0].value == filtro:
                    somma += row[4].value
        case filterType.NOME:  # caso nome
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
                if row[1].value.lower() == filtro.lower():
                    somma += row[4].value
        case filterType.GENERE:  # caso per genere
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
                if row[2].value == filtro:
                    somma += row[4].value
        case filterType.NAZIONALITÀ:  # caso per nazionalità
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
                if row[3].value == filtro:
                    somma += row[4].value
        case _:  # default
            somma = 0;
    return somma


def check_by_name(ws, nome):
    somma = somma_nuovi_nati(ws, nome, filterType.NOME)
    print("In tutto ci sono {} persone di nome {}.".format(somma, nome))
    print("Questa è la distribuzione nel corso degli anni: ")
    available_years = check_available_years(ws)
    name_year_distribution = dict((key, 0) for key in available_years)
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[1].value.lower() == nome.lower():
            name_year_distribution[row[0].value] += row[4].value
    fig, ax = plt.subplots()
    ax.hist(name_year_distribution.values(), available_years.sort())
    ax.set_xticklabels(str(available_years))
    ppl.show()
    ppl.close()


def check_by_year(ws, anno):
    somma = somma_nuovi_nati(ws, anno)
    print("In tutto nel {} sono nate {} persone.".format(anno, somma))


def check_by_nazionalità(ws, nazionalità):
    somma = somma_nuovi_nati(ws, nazionalità)
    print("In tutto nel {} sono nate {} persone.".format(nazionalità, somma))
