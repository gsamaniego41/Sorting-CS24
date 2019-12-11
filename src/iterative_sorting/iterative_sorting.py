# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Only swap when smallest is different from current index
        if cur_index != smallest_index:
            # print(f'Swap {arr[cur_index]} with {arr[smallest_index]}')
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
            # print(arr)
            # print('-----------------')

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    print(arr)
    for i in range(len(arr), -1, -1):
        for j in range(0, len(arr) - 1):
            print(arr[j], arr[j+1])
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
