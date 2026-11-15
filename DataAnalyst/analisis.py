##importar pandas y numpy
##leyendo un archivo csv

#import pandas as pd
#import numpy as np
#data = r"C:\Users\Tsp_JMontes_Bquilla\Downloads\reporte.csv"

#data = pd.read_csv(data)

#print(data.head())"""

import numpy as np

mi_arreglo = np.array([4,1,5,2])

print(mi_arreglo)

print(type(mi_arreglo))

mi_lista = [1,2,3,4]
print(mi_lista * 2) #out: [1, 2, 3, 4, 1, 2, 3, 4]

## el arreglo es una matriz dimensional lo cual su comporttamiento en las operaciones varia
print(mi_arreglo * 2) # out: [ 8  2 10  4]

print(np.sqrt(mi_arreglo))

## indexar
print(mi_arreglo[1])
print(mi_arreglo[::-1])