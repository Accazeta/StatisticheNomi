def checkAvailableYears(ws):
    lista_anni = []
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        if row[0].value not in lista_anni:
            lista_anni.append(row[0].value)
    return lista_anni

def checkMissingYears(lista_anni):
    lista_anni.sort()
    gap_years = []

    year = lista_anni[0]
    while year != lista_anni[-1]:
        if int(year) + 1 not in lista_anni:
            gap_years.append(int(year) + 1)
        year = year + 1