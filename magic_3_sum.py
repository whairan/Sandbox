
def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    # temp1 =0
    # temp2 = 0
    # temp3 = 0
    zero_sum_list = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j+1, len(arr)): 
                sum = arr[i] + arr[j] + arr [k]
                if sum == 0:
                    zero_sum_list.add(f"{arr[i]},{arr[j]},{arr[k]}")
                    # temp1 = i 
                    # temp2 = j 
                    # temp3 = k 
    return list(zero_sum_list)
    # return [temp1,temp3,temp3]



lst =  [10, 3, -4, 1, -6, 9]
find_zero_sum(lst)
print(find_zero_sum(lst))


"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n^3).
* Auxiliary space: O(1).
* Total space: O(n^2).
"""

# def find_zero_sum(arr):
#     answer = set() # To avoid duplicates.
#     # Sorting is only necessary for avoiding duplicates in the answer.
#     arr.sort()
#     n = len(arr)
#     for index_1 in range(n):
#         for index_2 in range(index_1 + 1, n):
#             for index_3 in range(index_2 + 1, n):
#                 sum_ = arr[index_1] + arr[index_2] + arr[index_3]
#                 if sum_ == 0:
#                     answer.add(f"{arr[index_1]},{arr[index_2]},{arr[index_3]}")
#     return list(answer)


# --list comprehension: 

# temp_list = [i for i in range(10, 500)]
# print(temp_list)
