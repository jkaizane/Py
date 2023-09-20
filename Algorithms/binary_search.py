""" Use of logarithms (logs) - the flip of exponentials.
 
expo is how many 10s do we multiply together to get 100

logs is Example: How many 2s multiply together to make 8?

Answer: 2 * 2 * 2 = 8, so we had to multiply 3 of the 2s to get 8

So the logarithm is 3 """

def binary_search(list, item):
# low and high keep track of which part of the list to search in
    low = 0
    high = len(list)-1
# while haven't narrowed down to one element
    while low <= high:
        mid = round((low + high) / 2)
        # check the middle element
        guess = list[mid]
        if guess == item:
            # found item
            return mid
        if guess > item:
            # the guess was too high
            high = mid - 1
        else:
            # the guess was too low
            low = mid + 1
    return None
# the item doesn't exist

# test data
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
        