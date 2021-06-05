def bubble_sort(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

arrey=[2,4,5,6,8,3,4]
bubble_sort(arrey)
