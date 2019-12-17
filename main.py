def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n): 
        min_idx = i 
        for j in range(i + 1, n): 
            if array[min_idx] > array[j]: 
                min_idx = j        
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def bubble_sort_generator(array):
    arraycopy = array.copy()
    while True:
        arrays = []
        n = len(arraycopy)
        for i in range(n):
            for j in range(n - i - 1):
                if arraycopy[j] > arraycopy[j+1]:
                    arraycopy[j], arraycopy[j+1] = arraycopy[j+1], arraycopy[j]
                arrays.append(list(arraycopy))
        yield arrays

def selection_sort_generator(array):
    arraycopy = array.copy()
    while True:
        arrays = []
        n = len(arraycopy)
        for i in range(n): 
            min_idx = i 
            for j in range(i + 1, n): 
                if arraycopy[min_idx] > arraycopy[j]: 
                    min_idx = j        
            arraycopy[i], arraycopy[min_idx] = arraycopy[min_idx], arraycopy[i]
            arrays.append(list(arraycopy))
        yield arrays


