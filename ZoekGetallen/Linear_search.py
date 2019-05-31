# This is how we define a function in Python
# We will see more about functions later
def linear_search(x, search_list):
    """
    Returns the index of the x if found in search_list
    Else returns -1
    """
    iterations = 0
    idx = 0
    while idx < len(search_list):
        iterations += 1
        if x == search_list[idx]:
            print('iterations = ' + str(iterations))
            return idx
        idx += 1
    return -1

print(linear_search(32, [4, 8, 45, 24, 10, 32, 9, 56]))
# Output:
# -------
# iterations = 6
# 5
print(linear_search(21, [4, 8, 45, 24, 10, 32, 9, 56]))
# Output:
# -------
# -1