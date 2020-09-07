# rpy2 library used to call r function
# more detailed documentation can be found at https://rpy2.github.io/doc/latest/html/robjects_robjects.html
import rpy2.robjects as ro

# used to exit program when user enters exit
import sys

def load_r_module(path_to_module):
    """[summary]

    Args:
        path_to_module (str): path to desired R module

    Returns:
        r: r process for specified module
    """

    # entrypoint to R process
    r=ro.r

    # load file
    r.source(path_to_module)

    return r

def call_r_increment(r, num_1, num_2):
    """call the function in the r module to increment the two specified variables

    Args:
        r (r): r process to call function
        num_1 (float): first number to increment
        num_2 (float): second number to increment

    Returns:
        tuple: incremented numbers with form (num_1 + 1, num_2 + 1)
    """
    # call r function
    incremented_vector = r.increment_numbers(num_1,num_2)
    return tuple(incremented_vector)

def validate_data(num):
    """if the string is a number, cast it, if not, reprompt the user

    Args:
        num (str): user inputted unber

    Returns:
        float: float representation of the number
    """
    # quit if the user passes in "Exit"
    if num == "exit":
        sys.exit()

    try: 
        # return the float representation of the string
        return float(num)

    # float cast throws a ValueError if unsuccessful
    except ValueError:

        # reprompt the user to enter a number
        print('Malformed Input. Please enter a number')
        num = input('Please Enter the first number. (Enter "exit" to quit): ')

        # recursively call validate_data until the user either exits or provides valid input
        return validate_data(num)

if __name__ == "__main__":
    # load the r module
    r = load_r_module('module.R')

    # repeat until the user exits
    while(True):

        # get first number
        num_1 = input('Enter the first number. (Enter "exit" to quit): ')
        num_1 = validate_data(num_1)

        # get second number
        num_2 = input('Enter the second number. (Enter "exit" to quit): ')
        num_2 = validate_data(num_2)

        # call r function to increment numbers
        incremented_numbers = call_r_increment(r,num_1, num_2)

        print('Incremented numbers are %f, %f' % incremented_numbers)

