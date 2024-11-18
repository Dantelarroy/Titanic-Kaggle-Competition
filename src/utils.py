# src/utils.py
'''En este archivo se agregaran:
Funciones para cargar y preprocesar los datos'''

# src/utils.py
import pandas as pd

def eliminar_columna(df: pd.DataFrame, columna: str):
        """Elimina una columna de un DataFrame."""
        if columna in df.columns:
            df = df.drop(columns=[columna])
            print(f"Columna '{columna}' eliminada exitosamente.")
        else:
            print(f"Error: La columna '{columna}' no existe en el DataFrame.")
        return df


def columnas_a_minusculas(df):
    """Convierte los nombres de todas las columnas a minúsculas."""
    df.columns = [col.lower() for col in df.columns]
    return df
