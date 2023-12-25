import pandas as pd

def procesar_dataframe(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        print("Existen valores faltantes en el DataFrame")
        df = df.dropna()  # Eliminar filas con valores faltantes
    
    # Verificar filas duplicadas
    if df.duplicated().any():
        print("Existen filas duplicadas en el DataFrame")
        df = df.drop_duplicates()  # Eliminar filas duplicadas
    
    # Verificar y eliminar valores atípicos
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    # Crear columna de categorías por edades
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['Categoria Edad'] = pd.cut(df['age'], bins=bins, labels=labels)
    
    return df

# Carga el archivo CSV descargado anteriormente (suponiendo que está guardado como 'datos_descargados.csv')
nombre_archivo_csv = 'datos_descargados.csv'
df = pd.read_csv(nombre_archivo_csv)

# Procesar el DataFrame
df_procesado = procesar_dataframe(df)

# Guardar el resultado como CSV
nombre_archivo_resultado = 'datos_procesados.csv'
df_procesado.to_csv(nombre_archivo_resultado, index=False)
