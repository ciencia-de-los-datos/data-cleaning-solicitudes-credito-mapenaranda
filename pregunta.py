"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    #
    
    df= df[df.columns[1:]]
    df.columns.values

    df['sexo']= df['sexo'].str.lower() 

    df['tipo_de_emprendimiento']= df['tipo_de_emprendimiento'].str.lower()

    df['idea_negocio']= df['idea_negocio'].str.lower()
    df['idea_negocio']=df['idea_negocio'].str.replace("-","_")
    df['idea_negocio']=df['idea_negocio'].str.replace("_"," ")
    df['idea_negocio']=df['idea_negocio'].str.strip()

    df['barrio']= df['barrio'].str.lower()
    df['barrio']=df['barrio'].str.replace("-","_")
    df['barrio']=df['barrio'].str.replace("_"," ")

    df['línea_credito']= df['línea_credito'].str.lower()
    df['línea_credito']=df['línea_credito'].str.replace("-","_")
    df['línea_credito']=df['línea_credito'].str.replace("_"," ")
    df['línea_credito']=df['línea_credito'].str.replace(".","")
    df['línea_credito']=df['línea_credito'].str.strip()

    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,dayfirst=True)

    df['monto_del_credito']=df['monto_del_credito'].str.replace(",","")
    df['monto_del_credito']=df['monto_del_credito'].str.replace("$","")
    df['monto_del_credito']=df['monto_del_credito'].str.strip()
    df['monto_del_credito'] = df['monto_del_credito'].apply(pd.to_numeric, downcast="integer", errors='ignore')
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    return df
