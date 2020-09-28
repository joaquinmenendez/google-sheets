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

Si vamos a trabajar en un archivo alojado en nuestra cuenta (o que se
nos a dado permisos) debemos primero:

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

- Utilizar el módulo `google-sheets.py` para operar sobre nuestra tabla.
  El siguiente ejemplo muestra cómo sería un posible uso del mismo.

```python
ID = "1hN9p7_IPSiaM-o6NL0qTO70W2Wqv7HyyPS1OvJvbXL0"  # NUESTRO PROYECTO
HOJA = 'Hoja 1'  # NOMBRE DE NUESTRA PRIMERA PESTAÑA
RANGO = f'{HOJA}!A:C'  # DEFINE EL RANGO EN EL QUE ESTAMOS TRABAJANDO

service = gs.initializeService()  # Crea el servicio
df = gs.exportDataToSheet(service,ID, RANGO)  # Lee los datos y los guarda
```
```bash
# Output
  col1 col2  col3
0    1    a    45
1    2    s    46
2    3    d    47
3   99   zz  1991
```
```python
df.loc[3] = [4,'w',48]  # Cambiamos campos (o agregamos nueva info)   
gs.exportDataToSheet(service,ID,RANGO,df)  # Exporta el df a una spreedsheat
```
```bash
Datos agregados
```

Puede encontrar un tutorial mas detallado
[aquí](https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c)


