def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        temp = arr[i]
        red = i-1
        while red >=0 and arr[red] > temp:
            arr[red+1] = red
    return arr


# faster implementation

def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
            j = j - 1
    return arr 
    
    
    
    
    
    