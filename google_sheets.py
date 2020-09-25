import pickle
import os.path
import pandas as pd
from googleapiclient.discovery import build

ID = "1hN9p7_IPSiaM-o6NL0qTO70W2Wqv7HyyPS1OvJvbXL0"  # Nuestro proyecto
HOJA = 'Hoja 1' # NOMBRE DE NUESTRA PRIMERA PESTAÑA
RANGO = f'{HOJA}!A:C' # DEFINE EL NOMBRE DE COLUMNAS

def main():
    # Carga credenciales  [Averiguar cuanto duran!]
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credenciales = pickle.load(token)
    else:
        raise AssertionError('''
        El archivo token.pickle no existe en el directorio local.
        Por favor verifique que ha corrido el archivo quickstart.py primero.
        ''')

    # Crea el servicio
    service = build('sheets', 'v4', credentials=credenciales)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ID,
                                range=RANGO).execute()
    values = result.get('values', [])
    df = pd.DataFrame(data= values[1:],
                      columns=values[0])
    print(df)

if __name__ == '__main__':
    main()
# Aqui agregare cosas para subir a otra hoja o modificar las columnas. Debo aprender como aun