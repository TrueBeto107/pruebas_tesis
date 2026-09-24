"""Módulo para la gestión de respaldos de base de datos.

Proporciona funcionalidad para crear respaldos automáticos de la base de datos
usando el comando 'flask backup'
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

from flask import Flask


def registrar_backup(app: Flask) -> None:
    """Registra un comando CLI en Flask para crear respaldos de base de datos.

    Registra el comando 'flask backup' que crea un respaldo SQL de la
    base de datos.
    El archivo de backup se guarda en el directorio Backups
    con un nombre que incluye la fecha y hora actual.

    Args:
        app (Flask): instancia de la aplicación Flask.

    """

    @app.cli.command("backup")
    def backup_command()-> str | None:
        """Crea un respaldo de la base de datos desde Flask.

        Returns:
            str | None: La ruta del archivo de backup creado,
            o None si hubo un error.

        """
        db_uri = app.config[
            "SQLALCHEMY_DATABASE_URI"
        ]
        match = re.match(
            r"postgresql\+psycopg2://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)",
            db_uri,
        )
        if not match:
            print("Error: No se pudo leer la URI de la base de datos")  # noqa: T201 para saber que es un print de error
            return None
        usuario, contrasenia, host, puerto, base_datos = match.groups()
        directorio_backup = app.config["DIRECTORIO_BACKUP"]
        directorio_backup.mkdir(exist_ok=True)
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo = directorio_backup / f"backup_{fecha}.sql"
        comando = (
            f"pg_dump -h {host} -p {puerto} -U {usuario} "
            f"-d {base_datos} -f {archivo}"
        )
        env = (os.environ.copy())
        env["PGPASSWORD"] = contrasenia

        try:
            resultado = subprocess.run(
                comando, shell=True, env=env, capture_output=True, text=True
            )
        except OSError:
            return None

        if resultado.returncode == 0:
            tamaño = Path(archivo).stat().st_size / 1024
            print(f"Backup creado: {archivo} ({tamaño:.2f} KB)")  # noqa: T201
            return str(archivo)
        return None
