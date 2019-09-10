# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):

        cur_index = i
        smallest_index = cur_index

        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x 

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    count = 1

    while count == 1:
        count = 0
        for i in range(0, len(arr) -1 ):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count = 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

list = [4,3, 5, 1, 6, 8, 2]
print(bubble_sort(list))