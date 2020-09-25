## Pasos

- Clonar este repositorio

```bash
git clone https://github.com/joaquinmenendez/google-sheets.git
# Posicionarse dentro del reposiorio. 
# Todas los pasos siguientes asumen que estamos en este directorio
cd google-sheets
```

- Activar un virtualenv e instalar las librerias requeridas.

> Linux/IOs

```bash
virtualenv .venv
source .venv/bin/activate
pip3 install --upgrade -r requirements.txt
```

> Windows

```bash
    virtualenv -p python3 .venv
    source .venv/Script/activate
    pip3 install --upgrade -r requirements.txt
```

Si vamos a trabajar en un archivo alojado en nuestra cuenta debemos
primero:

- Habilitar la
  [API de Google Sheets](https://developers.google.com/sheets/api/quickstart/python)
  para nuestra cuenta

- Descargar las credenciales (opción Dektop). Esto descargar un archivo
  llamado `credentials.json`. Guardarlo en el

- Ejecutar el script `quickstart.py`

```bash
python3 quickstart.py
```
La primera vez que ejecutemos este script nos va a mostrar un link, el
cual debemos copiar y pegar en nuestro explorador web. Ahi desde nuestra
cuenta de goolge autorizaremos a `Quickstart` a acceder a nuestra cuenta
con los scopes definidos en `quickstart.py` (por defecto reading and
writing).  
Una vez autoricemos esto se generará un archivo `token.pickle` en
nuestro repositorio local. No es necesario volver a correr
`quickstart.py` en el futuro a menos que nuestro `token.pickle` expire.

- Ejecutar el script `google_sheets.py`
```bash
python3 google_sheets.py
```

Por el momento `google_sheets.py` solo printea un DtaFrame en mi google drive account.
En caso de que usted desee interactuar con otro archivo modifique los parametros
`ID, HOJA, RANGO`.

Puede encontrar un tutorial mas detallado [aquí](https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c)


