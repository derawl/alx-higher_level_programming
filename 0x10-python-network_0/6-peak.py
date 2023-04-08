'''
module finds the peak in a list
'''

def find_peak(list_of_integers):
    """
    Takes a list of integer and returns the highest
    """
    low=0
    high = len(list_of_integers) - 1

    while low < high:
        mid = int((low + high) / 2) #find the middle of the list in absolute integer
        if(list_of_integers[mid] > list_of_integers[mid + 1]):
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]