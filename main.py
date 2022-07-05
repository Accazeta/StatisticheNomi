import functions as f
import traceback
from openpyxl import workbook, load_workbook, Workbook

try:
    wb = load_workbook('Nomi_Neonati_Bergamo.xlsx')
    ws = wb.active

    print("\nQueste sono i nomi delle colonne che ho trovato")
    try:
        for row in ws.iter_rows(min_col=ws.min_column, max_col=ws.max_column, min_row=ws.min_row, max_row=ws.min_row):
            for cell in row:
                print('|{}'.format(cell.value), end='')
        print('|')
    except:
        print(traceback.format_exc())

    try:
        # nome = input("Inserisci il nome che vuoi cercare: ")
        lista_anni = f.checkAvailableYears(ws)
        gap_years = f.checkMissingYears(lista_anni)
        if gap_years is None:
            print("Analizzo i dati dal {} al {}".format(lista_anni[0], lista_anni[-1]))
    except:
        print(traceback.format_exc())
except FileNotFoundError:
    print(traceback.format_exc())