# TO-DO: complete the helpe function below to merge 2 sorted arrays

arrA = [1, 4, 5, 6]
arrB = [2, 3, 9, 10]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(len(merged_arr)):
        if len(arrA) != 0 and len(arrB) != 0:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            else:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
        else:
            if len(arrA) != 0:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            if len(arrB) != 0:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
    
    return merged_arr

print(merge(arrA, arrB))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
