def burbuja(lista):#Ordenamiento de Burbuja
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    print("Ordenamiento Burbuja :")
    print(lista)

def quick_sort(lista):#Ordenamiento Quicksort
    quick_sort_aux(lista,0,len(lista)-1)
    print("Ordenamiento QuickSort :")
    print(lista)

def quick_sort_aux(lista,first,last):
    if first<last:
        pd = particion(lista,first,last)
        quick_sort_aux(lista,first,pd-1)
        quick_sort_aux(lista,pd+1,last)
 
def particion(lista,first,last):
    pivot = lista[first]
    izq = first+1
    der = last
    hecho = False
    while not hecho:
        while izq <= der and lista[izq] <= pivot:
            izq = izq + 1
        while lista[der] >= pivot and der >= izq:
            der = der -1
        if der < izq:
            hecho = True
        else:
            temp = lista[izq]
            lista[izq] = lista[der]
            lista[der] = temp
    temp = lista[first]
    lista[first] = lista[der]
    lista[der] = temp
    return der

if __name__ == '__main__':
    import sys
    burbuja(sys.argv[1])
    quick_sort(sys.argv[1])
