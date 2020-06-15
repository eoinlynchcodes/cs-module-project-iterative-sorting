# TO-DO: Complete the selection_sort() function below
def selection_sort(list):
    # loop through n-1 elements
    for i in range(len(list)):
        minimum_position = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(list)):
            if list[minimum_position] > list[j]:
                minimum_position = j
        # TO-DO: swap
        # Your code here
        temp = list[i]
        list[i] = list[minimum_position]
        list[minimum_position] = temp     

    return list


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - 1 ):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True

    return arr



'''

STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    # Your code here
    max = maximum + 1
    count = [0] * max

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(max):
        for c in range(count[a]):
            arr[i] = a
            i += 1
        return arr
