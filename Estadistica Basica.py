import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd # importando pandas

np.random.seed(2131982) # para poder replicar el random

datos = np.random.randn(5, 4) # datos normalmente distribuidos
print(datos)

# media arítmetica
print(datos.mean()) # Calcula la media aritmetica de

print(np.mean(datos)) # Mismo resultado desde la funcion de numpy

print("Esta es la media de las filas:", datos.mean(axis=1)) # media aritmetica de cada fila

print("Esta es la media de las filas:", datos.mean(axis=0)) # media aritmetica de cada columna

# mediana
print(np.median(datos))

np.median(datos, 0) # media aritmetica de cada columna

# Desviación típica
print(np.std(datos))

np.std(datos, 0) # Desviación típica de cada columna

# varianza
print(np.var(datos))

np.var(datos, 0) # varianza de cada columna

# moda
print(stats.mode(datos)) # Calcula la moda de cada columna
# el 2do array devuelve la frecuencia.

datos2 = np.array([1, 2, 3, 6, 6, 1, 2, 4, 2, 2, 6, 6, 8, 10, 6])
print(stats.mode(datos2)) # aqui la moda es el 6 porque aparece 5 veces en el vector.

# correlacion
print(np.corrcoef(datos)) # Crea matriz de correlación

# calculando la correlación entre dos vectores.
print("Matriz de correlación, dos muestras")
print(np.corrcoef(datos[0], datos[1]))

# covarianza
print("Matriz de covarianza")
print(np.cov(datos)) # calcula matriz de covarianza

# covarianza de dos vectores
print("Matriz de covarianza, dos variables")
print(np.cov(datos[0], datos[1]))

# usando pandas
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'], 
                        columns=['col1', 'col2', 'col3', 'col4'])
print(dataframe)

# resumen estadistadistico con pandas

print(dataframe.describe())

# sumando las columnas
print(dataframe.sum())

# sumando filas
print(dataframe.sum(axis=1))

print(dataframe.cumsum()) # acumulados

# media aritmetica de cada columna con pandas
print(dataframe.mean())

# media aritmetica de cada fila con pandas
print(dataframe.mean(axis=1))