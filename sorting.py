#Sorting


def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1):
        # keep track of whether we made a swap
        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
            # If no swap, list already sorted
            break
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    sorted_lst = []
    lst1_index = 0
    lst2_index = 0
    while (lst1_index < len(list1)) and (lst2_index < len(list2)):
        if list1[lst1_index] < list2[lst2_index]:
            sorted_lst.append(list1[lst1_index])
            lst1_index += 1
        else:
            sorted_lst.append(list2[lst2_index])
            lst2_index += 1
    if lst1_index < len(list1):
        for i in range(lst1_index, len(list1)):
            sorted_lst.append(list1[i])
    elif lst2_index < len(list2):
        for i in range(lst2_index, len(list2)):
            sorted_lst.append(list2[i])
    return sorted_lst


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) > 1:
        list1 = lst[0:(len(lst)/2)]
        list2 = lst[(len(lst)/2):]
        return merge_lists(merge_sort(list1), merge_sort(list2))

    else:
        return lst


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
