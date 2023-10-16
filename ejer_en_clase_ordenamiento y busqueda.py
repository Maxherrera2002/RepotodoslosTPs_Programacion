def merge_sort(numbers_):
    if len(numbers_) > 1:
        # Divide el arreglo en dos mitades
        half = len(numbers_) // 2
        left = numbers_[:half]
        right = numbers_[half:]

        # Llama recursivamente a merge_sort en ambas mitades
        left=merge_sort(left)
        right=merge_sort(right)

        # Combina las dos mitades ordenadas
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers_[k] = left[i]
                i += 1
            else:
                numbers_[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers_[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers_[k] = right[j]
            j += 1
            k += 1
    return numbers_

def bubble_sort(numbers):
    numbers_=numbers
    for i in range(len(numbers_)-1):
        for j in range(len(numbers_)-1):
            if numbers_[j]>numbers_[j+1]:
                aux=numbers_[j]
                numbers_[j]=numbers_[j+1]
                numbers_[j+1]=aux
    return numbers_

def selection_sort(numbers):
    numbers_=numbers
    array=[]
    while numbers_!=[]:
        
        for i in numbers_:
            if i==numbers_[0]:
                min=i
            elif(i<min):
                min=i
        numbers_.remove(min)
        array.append(min)        
    return array

def insert_sort(numbers):
    for i in range(1, len(numbers)):
        aux = numbers[i]
        j = i - 1
        while j >= 0 and aux < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = aux
    return numbers

numbers=[99,5,2,3,6,7,4,9,8,19,18,17,16,15,14,13,12,11,10]


print("Lista desordenada")
print(numbers)

print("Lista ordenada con bubble sort")
print(bubble_sort(numbers))

numbers=[99,5,2,3,6,7,4,9,8,19,18,17,16,15,14,13,12,11,10]

print("Lista ordenada con selection sort")
print(selection_sort(numbers))

numbers=[99,5,2,3,6,7,4,9,8,19,18,17,16,15,14,13,12,11,10]

print("Lista ordenada con insert sort")
print(insert_sort(numbers))

numbers=[99,5,2,3,6,7,4,9,8,19,18,17,16,15,14,13,12,11,10]

print("Lista ordenada con merge sort")
print(merge_sort(numbers))

