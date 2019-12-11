# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    # handles the remaining elements
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1

    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# print(merge([1, 4, 6], [3, 8, 15]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    right = merge_sort(arr[0:half])
    left = merge_sort(arr[half:len(arr)])

    return merge(left, right)


new_arr = [1, 4, 6, 3, 8, 5]
print(merge_sort(new_arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
