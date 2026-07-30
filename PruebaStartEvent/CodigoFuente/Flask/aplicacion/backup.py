# aplicacion/backup.py
import os
import subprocess#para ejecutar comandos en la terminal desde Python.

from datetime import datetime
from pathlib import Path #para manejar rutas de archivos y carpetas de forma fácil.
from flask import current_app # para acceder a la configuración de Flask.
import re #para trabajar con expresiones regulares y extraer información de la URI de la base de datos.

#En terminal solo ejecuta flask backup para hacer backup de la base de datos. El backup se guardará en la carpeta "backups" dentro del proyecto Flask.
def hacer_backup():
    """Crea un respaldo de la base de datos usando la configuración de Flask"""
    
    # 1. Obtener datos de la base de datos desde Flask
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI'] #'postgresql+psycopg2://admin_agent:admin_agent@localhost:5432/startevent_db'
    # 2. Extraer usuario, contraseña, host, puerto, base_datos
    match = re.match(r'postgresql\+psycopg2://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)', db_uri)
    if not match:
        print('Error: No se pudo leer la URI de la base de datos')
        return None
    
    USUARIO, CONTRASEÑA, HOST, PUERTO, BASE_DATOS = match.groups()
    
    # 3. Crear carpeta backups en StartEvent
    directorio_backup = Path(__file__).resolve().parents[3] / 'backups'
    directorio_backup.mkdir(exist_ok=True)
    
    # 4. Nombre del archivo con fecha
    fecha = datetime.now().strftime('%Y%m%d_%H%M%S')
    archivo = directorio_backup / f'backup_{fecha}.sql'
    # 5. Comando pg_dump
    comando = f'pg_dump -h {HOST} -p {PUERTO} -U {USUARIO} -d {BASE_DATOS} -f {archivo}'
    """
    Si quisieramos usar el otro formato .backup solo es cambiar la extensión del archivo y agregar el parámetro -Fc al comando pg_dump:
    archivo = directorio_backup / f'backup_{fecha}.backup'
    comando = f'pg_dump -h {HOST} -p {PUERTO} -U {USUARIO} -d {BASE_DATOS} -Fc -f {archivo}'
    """
    # 6. Ejecutar
    env = os.environ.copy() # con copia para no afectar otras variables de entorno
    env['PGPASSWORD'] = CONTRASEÑA #pg_dump necesita la contraseña para conectarse a la base de datos, y se la pasamos mediante la variable de entorno PGPASSWORD.
    
    try:
        resultado = subprocess.run(comando, shell=True, env=env, capture_output=True, text=True)
        
        if resultado.returncode == 0: # 0 significa que el comando se ejecutó correctamente.
            tamaño = os.path.getsize(archivo) / 1024 #calcular el tamaño del archivo en KB
            print(f'Backup creado: {archivo} ({tamaño:.2f} KB)')
            return str(archivo) #retorna la ruta del archivo de backup como cadena de texto. Esto puede ser útil si queremos usar esa ruta en otra parte del código, por ejemplo, para enviar el archivo por correo electrónico o para mostrarlo en una interfaz de usuario.
        else:
            print(f'Error: {resultado.stderr}')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None