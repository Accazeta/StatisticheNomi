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


def somma_nuovi_nati(ws, nome):
    somma = 0
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[1].value.lower() == nome.lower():
            somma += row[4].value
    return somma


def somma_nuovi_nati(ws, anno):
    somma = 0
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[0].value == anno:
            somma += row[4].value
    return somma


def somma_nuovi_nati(ws, nazionalità):
    somma = 0
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[3].value == nazionalità:
            somma += row[4].value
    return somma


def check_by_name(ws, nome):
    somma = somma_nuovi_nati(ws, nome)
    print("In tutto ci sono {} persone di nome {}.".format(somma, nome))
    print("Questa è la distribuzione nel corso degli anni: ")


def check_by_year(ws, anno):
    somma = somma_nuovi_nati(ws, anno)
    print("In tutto nel {} sono nate {} persone.".format(anno, somma))


def check_by_nazionalità(ws, nazionalità):
    somma = somma_nuovi_nati(ws, nazionalità)
    print("In tutto nel {} sono nate {} persone.".format(nazionalità, somma))