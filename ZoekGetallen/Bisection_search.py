
mylist = []
optellen = 0
while optellen < 1000:
    mylist.append(optellen)
    optellen = optellen + 0.01
    optellen = round(optellen, 2)
search_list = mylist

x = 5

iterations = 1
left = 0 # Determines the starting index of the list we have to search in
right = len(search_list)-1 # Determines the last index of the list we have to search in
mid = (right + left)//2 # In Python, // means floored division,

while search_list[mid] != x: # If this is not our search element
    # If the current middle element is less than x then move the left next to mid
    # Else we move right next to mid
    if  search_list[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
    mid = (right + left)//2
    iterations += 1
print ('iterations = ',str(iterations))
print(mid)