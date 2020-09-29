# -*- coding: utf-8 -*-
# author: Joaquin Menendez
# email: joaquin14@gmail.com

import pickle
import os.path
import pandas as pd
from googleapiclient.discovery import build


def initializeService(token_path='token.pickle', service = 'sheets'):
    '''
    Initialize a google service object. It use a pickle file to authenticate the user credential.
    The token files is generated by `quickstart.py`.
    :param token_path: (str) Path to the 'token.pickle' file
    :param service: (str) 'sheets' o 'drive'
    :return: (googleapiclient.discovery.Resource) Service object
    '''
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            credenciales = pickle.load(token)
    else:
        raise AssertionError('''
        El archivo token.pickle no existe en el directorio local.
        Por favor verifique que ha corrido el archivo quickstart.py primero.
        ''')
    if service == 'sheets':
        service = build('sheets', 'v4', credentials=credenciales)
        return service
    if service == 'drive':
        service = build('drive', 'v3', credentials=credenciales)
    return service


def getDatafromSheet(service, id, rango):
    '''
    Extract data from a specific spreadsheet file in a given range. It returns this information in a DataFrame format.
    :param service: (googleapiclient.discovery.Resource) Service object
    :param id: (str) Id correspondiente al file que vamos a usar (figura en la url del archivo)
    :param rango: (str) Rango de celdas en el cual se encuentra al informacion que queremos extraer
    :return: pandas.DataFrame
    '''
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=rango).execute()
    values = result.get('values', [])
    df = pd.DataFrame(data= values[1:],
                      columns=values[0])
    print(df.head())
    return df


def exportDataToSheet(service,id,rango,df):
    '''
    Export the data of a DataFrame object into a spread-sheet file in Google Sheets.
    :param service: (googleapiclient.discovery.Resource)  Service object
    :param id: (str) Id correspondiente al file que vamos a usar (figura en la url del archivo)
    :param rango: (str) Rango de celdas en el cual se encuentra al informacion que queremos extraer [i.e. 'A1:C3']
    :param df: (pandas.DataFrame)
    :return:  None
    '''
    vals = df.reset_index(drop=True).values.tolist()  # Convierte el df en una lista
    vals.insert(0, df.columns.tolist())  # Agrega las columnas como el primer elemento
    service.spreadsheets().values().update(
        spreadsheetId=id,
        range=rango,
        valueInputOption='RAW',
        body=dict(
            majorDimension='ROWS',
            values=vals
        )
    ).execute()  # Ejecuta la operacion
    print('Datos agregados')


def createSpreadsheet(service, title, folder=None, developerMetadata = None):
    spreadsheet = {
        'properties': {
            'title': title
        }
    }
    if developerMetadata:
        spreadsheet["developerMetadata"] = developerMetadata
    try:
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                fields='spreadsheetId').execute()
        if folder:
            drive = initializeService(token_path=folder['token'], service='drive')
            folderId = folder['id']
            res = drive.files().update(fileId=spreadsheet['spreadsheetId'], addParents=folderId,
                                       removeParents='root').execute()
        print(f"Spreadsheet ID: {spreadsheet.get('spreadsheetId')}")
    except Exception as e:
        print(e)
