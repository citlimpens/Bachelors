import numpy as np 
arreglo1 = np.array([1,2,3,4,5])
print(arreglo1)

lista1 = [1,2,3,4,5]
print(lista1)

arreglo_a = np.arange(2,10,2)
print(arreglo_a)


arreglo2 = np.array([[1,2,3],[4,5,6]])


#Valores de filas y columnasa
arreglo2.shape

#Numero de elementos
arreglo2.size



vector1 = np.array([4,5,6,7,8,9])
arreglo3 = vector1.reshape((2,3))
print(arreglo3)

"""
se puede llenar una matriz del tamaño 
deseado con puros 0 y 1 o con numeros aleatorios con random (entre 0 y 1)
y se pueden hacer opecariones usando esas matrices

"""
