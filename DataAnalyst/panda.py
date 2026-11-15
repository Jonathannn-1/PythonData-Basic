import pandas as pd
import numpy as np
import seaborn as sa #modulo que te da data frames
##pandas propone una estructura unidimensional llamada serie
# pero la estructura mas usada es el el dataframe bidimnesional

## se crea un dataFrame
registro_1= np.array(['Jonathan', 178, False])
registro_2= np.array(['Dayana', 150, False])
registro_3= np.array(['Maria', 155, True])
registro_4= np.array(['Sheryl', 166, False])
registro_5= np.array(['Miguel', 180, True])

lista = pd.DataFrame(data=[
    registro_1,
    registro_2,
    registro_3,
    registro_4,
    registro_5
], columns=[
    'nombre',
    'altura',
    'lesion'
])

print(lista)

##-------------------modulo iris para obtener un data frame

print(sa.get_dataset_names())## enlistar los dataframe existentes en en modulo seaborn

#cargando un dataset
iris = sa.load_dataset('iris')
print(iris.head())

##---------------------- importar datos---------------------------------------

#lo más habitual es leer datos de archivos externos, y para ello tendremos que tratar 
# con directorios. La Biblioteca Estándar de Python incluye el módulo os para trabajar 
# con rutas de archivos y directorios:

import os

print(os.path.isfile('DimCity.csv'))

leer_csv = pd.read_csv('DimCity.csv')
print(leer_csv)

leer_excel = pd.read_excel('ENTIDADES DINAMICAS 03 DE JUNIO_2DO CARGUE.xlsx')
print(leer_excel)

leer_json = pd.read_json('prueba.json')
print(leer_json)


#quedamos ppor Explorar un DataFrame