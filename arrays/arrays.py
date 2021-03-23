"""Ejercicios con vectores en python."""

array = [
        int(item) for item in input(
            "enter element in array : "
            ).split()
        ]


def sum_sub_prod_array(a1, a2):
    """Calculate sum , subtraction y product of two arrays."""
    v3_sum = sum_array(a1, a2)
    v3_sub = sub_array(a1, a2)
    v3_prod = prod_array(a1, a2)
    return v3_sum, v3_sub, v3_prod


def sum_elements(array):
    """Calculate sum of all elements in a array."""
    acum = 0
    for i in range(len(array)):
        acum += array[i]
    return acum


def prod_elements(array):
    """Calculate product of all elements in a array."""
    acum = 1
    for i in range(len(array)):
        acum = acum * array[i]
    return acum


def sum_array(v1, v2):
    """Sum two arrays."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3


def sub_array(v1, v2):
    """Subtract two arrays."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]-v2[i])
    return v3


def prod_array(v1, v2):
    """Product two arrays."""
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]*v2[i])
    return v3


def big_small_number(array):
    """Get the largest and smallest number in a array."""
    bigger = max(array, key=int)
    smaller = min(array, key=int)
    return bigger, smaller


def count_even_odd_prime(array):
    """Count the even, odd and prime of a vector."""
    even = 0
    odd = 0
    prime = 0
    for v in array:
        if v % 2 == 0:
            even += 1
        if v % 2 != 0:
            odd += 1
        if is_prime(v):
            prime += 1
    return even, odd, prime


def is_prime(num):
    """Validate if a number is prime."""
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def split_array(array):
    """Split a array in two arrays."""
    long = len(array)
    a1 = []
    a2 = []
    if long % 2 == 0:
        for i in range(0, (int)(long/2)):
            a1.append(array[i])
        for i in range((int)(long/2), (int)(long)):
            a2.append(array[i])
        return a1, a2
    else:
        array.pop((int)(len(array)/2))
        long = len(array)
        for i in range(0, (int)(long/2)):
            a1.append(array[i])
        for i in range((int)(long/2), (int)(long)):
            a2.append(array[i])
        return a1, a2


def is_simetric(array):
    """Validate if a array is simetric."""
    a1, a2 = split_array(array)
    if a1 == list(reversed(a2)):
        return True
    else:
        return False


def union(a1, a2):
    """Union of two arrays."""
    union = a1 + a2
    return union


def intersection(a1, a2):
    """Intersection of two arrays."""
    inter = [value for value in a1 if value in a2]
    return inter


def DiffAB(a1, a2):
    """Diff of two arrays."""
    return (
        list(
            list(set(a1)-set(a2)) + list(set(a2)-set(a1))
            )
        )


def DiffBA(a1, a2):
    """Diff of two arrays."""
    return (
        list(
            list(set(a2)-set(a1)) + list(set(a1)-set(a2))
            )
        )


print(f"array base : {array}\n")


print(f"sumatoria del array {array} : {sum_elements(array)}")
print(f"productoria del array {array} : {prod_elements(array)}")
bigger, smaller = big_small_number(array)
print(f'numero mayor : {bigger}\nnumero menor : {smaller}\n')


even, odd, prime = count_even_odd_prime(array)
print(f'pares : {even} - impares : {odd} - primos : {prime}\n')


array1 = [
        int(item) for item in input(
            "enter elements of array 1 : "
            ).split()
        ]
array2 = [
        int(item) for item in input(
            "enter elements of array 2 : "
            ).split()
        ]

if len(array1) == len(array2):
    sum_ar, sub_ar, produc_array = sum_sub_prod_array(array1, array2)
    print(f'suma de los vectores : {sum_ar}')
    print(f'resta de los vectores : {sub_ar}\n')
else:
    print("both vectors must be the same size \n")


print(f"array : {array}")
print(f'numero mas repetido : {max(set(array), key=array.count)}\n')

print(f"array : {array}")
a1, a2 = split_array(array.copy())
print("nuevos vectores despues de dividir")
print(f'array 1 : {a1}')
print(f'array 2 : {a2}')
sum_ar, sub_ar, produc_array = sum_sub_prod_array(array1, array2)
print(f'suma del array 1 y array 2 : {sum_ar}')
print(f'productoria de los array 1 y array 2 : {produc_array}\n')

print(f"el array {array} es simetrico ? : {is_simetric(array.copy())}\n")

print(f"Arrays : {array1} - {array2}")
print(f"Union : {union(array1, array2)}")
print(f"Interseccion : {intersection(array1, array2)}")
print(f"Diff(A-B) : {DiffAB(array1, array2)}")
print(f"Diff(BA-) : {DiffBA(array1, array2)}")
