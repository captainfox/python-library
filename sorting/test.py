# timing 7 different Python sorting algorithms with a list of integers
# each function is given the same list (fresh copy each time)
# tested with Python24       vegaseat      21jan2006

import random	# for generating random numbers
import time		# for timing each sort function with time.clock()

DEBUG = False	# set True to check results of each sort

N = 10000		# number of elements in list
list1 = []		# list of integer elements

for i in range(0, N):
    list1.append(random.randint(0, N-1))

#print list1  # test

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# declare the @ decorator just above each sort function, invokes print_timing()
@print_timing
def adaptive_merge_sort(list2):
    """adaptive merge sort, built into Python since version 2.3"""
    list2.sort()

@print_timing
def bubble_sort(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
    return arr

# selection sort
@print_timing
def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]  # swap
      
# insertion sort
@print_timing
def insertion_sort(list2):
    for i in range(1, len(list2)):
        save = list2[i]
        j = i
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save
  
# quick sort
@print_timing
def quick_sort(a):
    if len(a) <= 1: return a
    pivot = a.pop()
    before = [x for x in a if x <= pivot]
    after = [x for x in a if x > pivot]
    return quick_sort(before) + [pivot] + quick_sort(after)

# heap sort
@print_timing
def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)

# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1

# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k

# merge sort
@print_timing
def merge_sort(list2):
    merge_sort_r(list2, 0, len(list2) -1)

# merge sort recursive (used by merge_sort)
def merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)

# merge (used by merge_sort_r)
def merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    while i <= sred and j <= last:
        if list2 [i] <= list2 [j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2 [j])
            j += 1
    while i <= sred:
        helper_list.append(list2[i])
        i +=1
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list [k]

# test sorted list by printing the first 10 elements
def print10(list2):
    for k in range(10):
        print list2[k],
    print


# run test if script is executed
if __name__ == "__main__" :
    print("timing 7 sorting algorithms with a list of {} integers:".format(N))
    # make a true copy of list1 each time
    list2 = list(list1)
    adaptive_merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    bubble_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    heap_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    insertion_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    quick_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    selection_sort(list2)
    if DEBUG:
        print10(list2)
    # final test
    list2 = list(list1)
    if DEBUG:
        print "final test: ",
        print10(list2)

    #raw_input( "Press Enter to continue..." )

"""
typical results:
timing 7 sorting algorithms with a list of 1000 integers:
adaptive_merge_sort took 0.560ms
bubble_sort took 269.691ms
heap_sort took 13.556ms
insertion_sort took 130.870ms
merge_sort took 19.272ms
quick_sort took 6.849ms
selection_sort took 120.291ms
"""
