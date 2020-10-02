# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # check base case
    it = 1
    if r >= l:
        mid = l+(r-l)/2
        print("the mid index is {} and vaule is {}".format(mid, arr[mid]))
        # if element is present in the middle of the array
        if arr[mid] == x:
            return mid
            print("the record found ".format(arr[mid]))
        # if element in smaller then mid then it can only be present in left sub array
        elif arr[mid] > x:
            print("In {} iteration the middle value is {} so running in lest sub set".format(it, arr[mid]))
            return binarySearch(arr, l, mid-1, x)
        # else element can only be present in right sub array
        else:
            print("In {} iteration the middle value is {} so running in right sub set".format(it, arr[mid]))
            return binarySearch(arr, mid+1, r, x)
    else :
        # element is not in the list
        return -1

# Test array
arr = [3,5,8,10,34,12]
x = 10


# function call
print("length of array is {}".format(len(arr)))
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in the array")

    
