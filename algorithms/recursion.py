# Examples of recursive algorithms. Understanding these will help when you approach
# Functional Programming, especially those that do not make use of variables.

def countdown(x):

    # A recursive procedure (does not return a value) that has the effect of a while/for loop
    # to achieve a count-down.

    print(x)
    if x > 0:
        countdown(x - 1)


countdown(10)


def binary_search(item, items_list):

    # Basic approach: If the list contains no values then it cannot match the target.
    # Find the midpoint of the list and compare to the target item. If it matches then return
    # True because it has been found. If the item at the midpoint is larger than the target item
    # start the process again but focussing only on the 'left-hand' side of the list. If the
    # item at the midpoint is smaller than the target then start again searching the right-hand
    # side of the list. In both cases, exclude the current midpoint from the new lists as you know
    # the item won't be found there.

    mid = len(items_list) // 2

    if len(items_list) == 0:
        return False
    elif items_list[mid] == item:
        return True
    elif items_list[mid] < item:
        return binary_search(item, items_list[mid + 1:])
    else:
        return binary_search(item, items_list[:mid])


print(binary_search(2, [1,2,3,4,5,6]))


def sum_values(values_list):

    # Basic approach: If the list doesn't have any items, its sum is 0. If it contains only one
    # item, its sum is the value of that item. These are the base cases.
    # If there are more than 1 items, return the value of the first item in the list (the list's
    # head) added to the sum of all remaining items in the list (the list's tail).

    if len(values_list) == 0:
        return 0

    else:
        return values_list[0] + sum_values(values_list[1:])


print(sum_values([1, 2, 3, 4, 5]))


def is_prime(p, i=2):

    # Parameter i is used to compare p to progressively larger factors (i). Default value of 2
    # is specified so that the function can be called with just the value to test for primality.

    if p == 1:
        return False

    elif p == 2:
        return True

    elif i*i > p:
        return True

    elif p % i == 0:
        return False

    else:
        return is_prime(p, i + 1)


print(is_prime(163))
