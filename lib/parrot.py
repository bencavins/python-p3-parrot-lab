

def parrot(my_string="Squawk!"):
    print(my_string)
    return my_string


# example of a useful default parameter
def sort(my_list, reverse=False):
    if reverse:
        # sort descending
        pass
    else:
        # sorts ascending
        pass

# don't need to pass anything if we want to sort ascending
sort([])
# we only need to pass True if we want to sort descending
sort([], True)