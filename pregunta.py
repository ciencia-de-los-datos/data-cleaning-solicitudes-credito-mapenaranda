"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Cargamos el archivo y eliminamos de columna innecesaria
    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])
    # Eliminamos duplicados y valores nulos
    df = df.dropna().drop_duplicates()

    # Normalizamos las columnas de sexo, tipo de emprendimiento, idea de negocio y línea de crédito con una función lambda
    normalize_str = lambda x: x.lower().replace('_', ' ').replace('-', ' ').strip()
    df['sexo'] = df['sexo'].apply(normalize_str)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(normalize_str)
    df['idea_negocio'] = df['idea_negocio'].apply(normalize_str)
    df['línea_credito'] = df['línea_credito'].apply(normalize_str)
    #Para la columna barrio reemplazamos _ por - y luego - por espacio porque hay valores que tienen _ y otros que tienen - y así quedan todos iguales
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace('_', '-').replace('-', ' '))

    # Convertimos monto del credito a número
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '').str.replace('$', '', regex=False).str.replace(' ', '').astype(float)
    # Cambiamos el formato de la fecha de la columna fecha_de_beneficio
    #df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
    # Eliminamos duplicados y valores nulos
    df = df.drop_duplicates().dropna()

    return df