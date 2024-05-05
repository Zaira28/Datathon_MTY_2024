import datetime  as dt
import pandas as pd

# Mapeamos el 1 a las temporadas de interés
# 1-8 enero 
# 2-15 abril
# 20 julio - 27 agosto
# 16 - 31 diciembre
def periodo_col(date):
    if (dt.datetime(2023, 1, 1) <= date <= dt.datetime(2023, 1, 8) or
        dt.datetime(2023, 4, 2) <= date <= dt.datetime(2023, 4, 14) or
        dt.datetime(2023, 7, 20) <= date <= dt.datetime(2023, 8, 27) or
        dt.datetime(2023, 12, 16) <= date <= dt.datetime(2023, 12, 31) or
        dt.datetime(2024, 1, 1) <= date <= dt.datetime(2024, 1, 8) or
        dt.datetime(2024, 4, 2) <= date <= dt.datetime(2024, 4, 14) or
        dt.datetime(2024, 7, 20) <= date <= dt.datetime(2024, 8, 27) or
        dt.datetime(2024, 12, 16) <= date <= dt.datetime(2024, 12, 31)):
        return 1
    else:
        return 0


# Función para mapear estos intervalos a una columna de 0 a 3
def horario(hour):
    if hour in range(0,7):
        # Para la madrugada
        return 0
    elif hour in range(6,13):
        # Para la mañana
        return 1
    elif hour in range(13,20):
        # Para la tarde
        return 2
    else:
        # Para la noche
        return 3


def mapear_columna(df, nombre_columna):
    mapeo_columna, _ = pd.factorize(df[nombre_columna])
    return mapeo_columna


def mapear_y_agregar_columna(df, nombre_columna_original, nombre_columna_nueva):
    df[f'Mapeo_{nombre_columna_original}'] = mapear_columna(df, nombre_columna_original)
    return df

def filter_row(passengers,capacity):
    if (passengers > capacity):
        return capacity
    else:
        return passengers